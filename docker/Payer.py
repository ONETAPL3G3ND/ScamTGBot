from coinbase_commerce.client import Client
import coinbase_commerce.api_resources.charge
import requests
import json
from aiohttp import web
import aiohttp


class Payer:
    def __init__(self, *, bot):
        self.coinbase_commerce_api_key = '---'
        self.client = Client(api_key=self.coinbase_commerce_api_key)
        self.bot = bot

    def GeneratePaymentLink(self, price, message):
        url = "https://api.commerce.coinbase.com/charges"
        headers = {
            "Content-Type": "application/json",
            "X-CC-Api-Key": self.coinbase_commerce_api_key,
            "X-CC-Version": "2018-03-22"
        }
        data = {
            'name': 'PVP777',
            'description': 'PVP777',
            'local_price': {'amount': price, 'currency': 'RUB'},
            'pricing_type': 'fixed_price',
            'metadata': {'customer_telegram_id': message.chat.id}
        }
        response = requests.post(url, headers=headers, json=data)
        response_data = response.json()
        payment_link = response_data["data"]['hosted_url']
        return payment_link

    async def SetWebhook(self, dp):
        global_ip = await self.GetGlobalIp()
        app = web.Application()
        app.add_routes([web.post('/webhook', self.HandleCoinbaseCommercePayment)])
        runner = web.AppRunner(app)
        await runner.setup()
        site = web.TCPSite(runner, global_ip, 8443)
        await site.start()
        await self.bot.set_webhook(f'https://{global_ip}:8443/webhook')

    async def HandleCoinbaseCommercePayment(self, request: web.Request):
        data = await request.json()
        event_id = data['event']['id']
        charge_id = data['event']['data']['resource']['id']
        charge = coinbase_commerce.api_resources.charge.Charge.retrieve(charge_id,
                                                                        api_key=self.coinbase_commerce_api_key)
        user_id = charge.metadata['customer_telegram_id']
        await self.bot.send_message(user_id, "Ваш платеж успешно прошел! Спасибо за оплату.")
        return web.Response(text=json.dumps({'success': True}))

    async def GetGlobalIp(self):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://api.ipify.org?format=json') as resp:
                data = await resp.json()
                return data['ip']
