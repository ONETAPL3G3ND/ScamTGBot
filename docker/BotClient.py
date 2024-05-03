import Text
from aiogram.types import Message
import aiogram
import Payer


class BotClient:
    text = Text.Text()
    def __init__(self, bot, dp):
        self.bot = bot
        self.dp = dp
        self.payer = Payer.Payer(bot=bot)

        self.cladphoto = "https://cs10.pikabu.ru/post_img/big/2020/08/23/6/1598172894151698637.jpg"

        self.product = {
            "WhiteWidow1": {"Doze": "1", "Price": 2600,"imagepath":"https://www.istockphoto.com/ru/%D1%84%D0%BE%D1%82%D0%BE/%D0%BC%D0%B0%D1%80%D0%B8%D1%85%D1%83%D0%B0%D0%BD%D0%B0-%D0%BA%D0%B2%D1%96%D1%82%D0%BA%D0%BE%D0%B2%D0%B8%D0%B9-%D0%B1%D1%83%D1%82%D0%BE%D0%BD-%D1%84%D0%BE%D0%BD%D1%83-%D0%BC%D0%B5%D0%B4%D0%B8%D1%87%D0%BD%D0%B8%D0%B9-%D0%BA%D0%B0%D0%BD%D0%B0%D0%B1%D1%96%D1%81-gm1371072583-440485155", "Descript": """Мощнейший, аутентичный сорт который снимет с Вас тапки!!! Семена от сидбанка Sensi Seeds, прямиком из Амстердама. 90% Индики / 10% Сатива / ТГК 20%. Несмотря на то, что данный сорт Индико-доминантный, хай-эффект у него очень сильный и продолжительный. Вас буквально подбросит до небес от эйфории, а после прибьет к дивану мощным стоуном на пару часов. Хвойно - цитрусовый аромат, дым отдает легким холодком!Для оформления заказа нажми 'Сделать заказ'"""},
            "WhiteWidow2": {"Doze": "2", "Price": 3760,"imagepath":"https://www.istockphoto.com/ru/%D1%84%D0%BE%D1%82%D0%BE/%D0%BC%D0%B0%D1%80%D0%B8%D1%85%D1%83%D0%B0%D0%BD%D0%B0-%D0%BA%D0%B2%D1%96%D1%82%D0%BA%D0%BE%D0%B2%D0%B8%D0%B9-%D0%B1%D1%83%D1%82%D0%BE%D0%BD-%D1%84%D0%BE%D0%BD%D1%83-%D0%BC%D0%B5%D0%B4%D0%B8%D1%87%D0%BD%D0%B8%D0%B9-%D0%BA%D0%B0%D0%BD%D0%B0%D0%B1%D1%96%D1%81-gm1371072583-440485155", "Descript": """Мощнейший, аутентичный сорт который снимет с Вас тапки!!! Семена от сидбанка Sensi Seeds, прямиком из Амстердама. 90% Индики / 10% Сатива / ТГК 20%. Несмотря на то, что данный сорт Индико-доминантный, хай-эффект у него очень сильный и продолжительный. Вас буквально подбросит до небес от эйфории, а после прибьет к дивану мощным стоуном на пару часов. Хвойно - цитрусовый аромат, дым отдает легким холодком!Для оформления заказа нажми 'Сделать заказ'"""},
            "AMNESIA1": {"Doze": "1", "Price": 4800,"imagepath":"https://img.hs420.net/uploads/monthly_2020_09/02.png.59fa154d14a9a041d67c1f91bd10d836.png", "Descript": """Amnesia Haze. Sativa 80% / Indica 20% / THC 20%. Неоднократный победитель мировых чемпионатов и постоянный участник топовых рейтингов. Вероятно, самая известная сатива в мире, обладающая ярко выраженным настойчивым эффектом эйфории и безудержного веселья. Обладает приятным сладким фруктовым вкусом. Идеально подойдет для употребления в компании в светлое время суток. Amnezia Haze – сорт, который должен попробовать каждый.Для оформления заказа нажми 'Сделать заказ'"""},
            "Issol2": {"Doze": "2г", "Price": 3500,"imagepath":"https://img.hs420.net/uploads/monthly_2020_09/02.png.59fa154d14a9a041d67c1f91bd10d836.png", "Descript": """Душистый, мягкий, липкий, как смола хвойного дерева, гашиш, обладает отличным качеством и не крошится. Произведено искусными руками по технологии ICE-O-LATOR. Содержание ТГК достигает более 40%! Гашиш произведен из лучших сортов шишек. Плотный дым уже с первой затяжки, который уничтожит даже самую бессовестную толерантность. Минимальный расход натурального продукта. Будьте внимательны с дозировкой.Для оформления заказа нажми 'Сделать заказ'"""},
            "EURO3": {"Doze": "3г", "Price": 5300,"imagepath":"https://img.hs420.net/uploads/monthly_2020_09/02.png.59fa154d14a9a041d67c1f91bd10d836.png", "Descript": """Возвращение легенды! Отличная печать натурального и мощного "еврика", которая заставит Вас окунуться в океан ностальгии. Аромат сортовых шишек и приятный натур, который Вы получите по отличной цене! Лепится от нагрева зажигалки.Для оформления заказа нажми 'Сделать заказ'"""},
            "PVP05": {"Doze": "0.5г", "Price": 1530,"imagepath":"https://imageio.forbes.com/specials-images/imageserve/107d6249ee774946a830b805279ca638/640x0.jpg?height=400&width=711&fit=bounds", "Descript": """A-PVP Crystall - сильнейшие кристаллы A-PVP высокого качества. Наши кристаллы гарантируют мощную стимуляцию с ярко выраженной эйфорией. Будьте аккуратны с дозировками, один из сильнейших стимуляторов с эффектом эйфоретика. При употреблении заставит Вас почувствовать прилив энергии, желание общаться, приятные волны эйфории, чувствительность к людям, сексуальное возбуждение и коммуникабельность во всем!Для оформления заказа нажми 'Сделать заказ'"""},
            "PVP1": {"Doze": "1г", "Price": 2730,"imagepath":"https://imageio.forbes.com/specials-images/imageserve/107d6249ee774946a830b805279ca638/640x0.jpg?height=400&width=711&fit=bounds", "Descript": """A-PVP Crystall - сильнейшие кристаллы A-PVP высокого качества. Наши кристаллы гарантируют мощную стимуляцию с ярко выраженной эйфорией. Будьте аккуратны с дозировками, один из сильнейших стимуляторов с эффектом эйфоретика. При употреблении заставит Вас почувствовать прилив энергии, желание общаться, приятные волны эйфории, чувствительность к людям, сексуальное возбуждение и коммуникабельность во всем!Для оформления заказа нажми 'Сделать заказ'"""},
            "PVP2": {"Doze": "2г", "Price": 3530,"imagepath":"https://imageio.forbes.com/specials-images/imageserve/107d6249ee774946a830b805279ca638/640x0.jpg?height=400&width=711&fit=bounds", "Descript": """A-PVP Crystall - сильнейшие кристаллы A-PVP высокого качества. Наши кристаллы гарантируют мощную стимуляцию с ярко выраженной эйфорией. Будьте аккуратны с дозировками, один из сильнейших стимуляторов с эффектом эйфоретика. При употреблении заставит Вас почувствовать прилив энергии, желание общаться, приятные волны эйфории, чувствительность к людям, сексуальное возбуждение и коммуникабельность во всем!Для оформления заказа нажми 'Сделать заказ'"""},
            "AMF1": {"Doze": "1г", "Price": 1830,"imagepath":"https://kazan.mcmk.su/sites/testkazan/files/1691304524/amf1.jpg", "Descript": """Aмфетaмин VНQ - Высококачественный амфетамин для наших клиентов. При употреблении заставит Вас почувствовать сильный прилив сил, отличную стимуляцию и даже уловимый поток эйфории, разносящийся мурашками по всему телу. Эффект продолжительный и ярко выраженный. Имеет свойственный для амфетамина запах. Мы стараемся делать перевес в каждом кладе!Для оформления заказа нажми 'Сделать заказ'"""},
            "AMF2": {"Doze": "2г", "Price": 3000,"imagepath":"https://kazan.mcmk.su/sites/testkazan/files/1691304524/amf1.jpg", "Descript": """Aмфетaмин VНQ - Высококачественный амфетамин для наших клиентов. При употреблении заставит Вас почувствовать сильный прилив сил, отличную стимуляцию и даже уловимый поток эйфории, разносящийся мурашками по всему телу. Эффект продолжительный и ярко выраженный. Имеет свойственный для амфетамина запах. Мы стараемся делать перевес в каждом кладе!Для оформления заказа нажми 'Сделать заказ'"""},
            "MEF05": {"Doze": "0.5г", "Price": 1580,"imagepath":"https://legalizebelarus.org/wp-content/uploads/2023/05/63c5fc748136f.jpg", "Descript": """Представляем вашему вниманию, по своему уникальный Эйфоретик Мефедрон Кристалл [VHQ]! Наш Мефедрон как выше подметили "уникален" своим чистейшем синтезом, изготовлен на профессиональном оборудовании в лабораторных условиях! Благодаря грамотным химикам, вы ощутите более долгую эйфорию и наслаждение! Начинайте с меньшего к большему, а не наоборот и ощути те невероятные эмоции вместе с нашим Мефедроном Кристалл [VHQ]!Для оформления заказа нажми 'Сделать заказ'"""},
            "MEF1": {"Doze": "1г", "Price": 2540,"imagepath":"https://legalizebelarus.org/wp-content/uploads/2023/05/63c5fc748136f.jpg", "Descript": """Представляем вашему вниманию, по своему уникальный Эйфоретик Мефедрон Кристалл [VHQ]! Наш Мефедрон как выше подметили "уникален" своим чистейшем синтезом, изготовлен на профессиональном оборудовании в лабораторных условиях! Благодаря грамотным химикам, вы ощутите более долгую эйфорию и наслаждение! Начинайте с меньшего к большему, а не наоборот и ощути те невероятные эмоции вместе с нашим Мефедроном Кристалл [VHQ]!Для оформления заказа нажми 'Сделать заказ'"""},
            "MEF2": {"Doze": "2г", "Price": 4640,"imagepath":"https://legalizebelarus.org/wp-content/uploads/2023/05/63c5fc748136f.jpg", "Descript": """Представляем вашему вниманию, по своему уникальный Эйфоретик Мефедрон Кристалл [VHQ]! Наш Мефедрон как выше подметили "уникален" своим чистейшем синтезом, изготовлен на профессиональном оборудовании в лабораторных условиях! Благодаря грамотным химикам, вы ощутите более долгую эйфорию и наслаждение! Начинайте с меньшего к большему, а не наоборот и ощути те невероятные эмоции вместе с нашим Мефедроном Кристалл [VHQ]!Для оформления заказа нажми 'Сделать заказ'"""},

        }

    async def CommandStartHandler(self, message: Message) -> None:
        KeyBoard = [
            [aiogram.types.InlineKeyboardButton(text="🚬Оформить заказ🚬", callback_data="order"),
             aiogram.types.InlineKeyboardButton(text="❓Информация❓", callback_data="information")]
        ]
        keyboard = aiogram.types.InlineKeyboardMarkup(inline_keyboard=KeyBoard)
        await message.answer_photo(photo=self.cladphoto , caption=self.text.start, reply_markup=keyboard)


    async def CallBackHandler(self, callback: aiogram.types.CallbackQuery):
        if callback.data == "order":
            await self.bot(aiogram.methods.delete_message.DeleteMessage(chat_id=callback.message.chat.id,
                                                               message_id=callback.message.message_id))
            await self.Order(callback)
        elif callback.data == "productlist":
            await self.bot(aiogram.methods.delete_message.DeleteMessage(chat_id=callback.message.chat.id,
                                                               message_id=callback.message.message_id))
            await self.ProductList(callback)
        elif callback.data == "backtostart":
            await self.bot(aiogram.methods.delete_message.DeleteMessage(chat_id=callback.message.chat.id,
                                                               message_id=callback.message.message_id))
            await self.CommandStartHandler(callback.message)
        elif callback.data == "backtoproduct":
            await self.bot(aiogram.methods.delete_message.DeleteMessage(chat_id=callback.message.chat.id,
                                                                        message_id=callback.message.message_id))
            await self.ProductList(callback)
        elif callback.data == "information":
            await self.bot(aiogram.methods.delete_message.DeleteMessage(chat_id=callback.message.chat.id,
                                                                        message_id=callback.message.message_id))
            await self.Information(callback)
        else:
            try:
                callbackdata = callback.data.split("_")
                if callbackdata[0] == "product":
                    await self.bot(aiogram.methods.delete_message.DeleteMessage(chat_id=callback.message.chat.id,
                                                                                message_id=callback.message.message_id))
                    await self.ProductHandler(callback)
                elif callbackdata[0] == "buy":
                    await self.BuyProduct(callback)

            except:
                ...
    async def Order(self, callback: aiogram.types.CallbackQuery):
        KeyBoard = [
            [aiogram.types.InlineKeyboardButton(text="ЦАО", callback_data="productlist"),
             aiogram.types.InlineKeyboardButton(text="СВАО", callback_data="productlist")],
            [aiogram.types.InlineKeyboardButton(text="ЮВАО", callback_data="productlist"),
             aiogram.types.InlineKeyboardButton(text="ЮЗАО", callback_data="productlist")],
            [aiogram.types.InlineKeyboardButton(text="СЗАО", callback_data="productlist"),
             aiogram.types.InlineKeyboardButton(text="САО", callback_data="productlist")],
            [aiogram.types.InlineKeyboardButton(text="ВАО", callback_data="productlist"),
             aiogram.types.InlineKeyboardButton(text="ЮАО", callback_data="productlist")],
            [aiogram.types.InlineKeyboardButton(text="ЗАО", callback_data="productlist"),
             aiogram.types.InlineKeyboardButton(text="Троицкий", callback_data="productlist")],
            [aiogram.types.InlineKeyboardButton(text="Зеленоградский", callback_data="productlist")],
             [aiogram.types.InlineKeyboardButton(text="Новомосковский", callback_data="productlist")],
            [aiogram.types.InlineKeyboardButton(text="Назад", callback_data="backtostart")]
        ]
        keyboard = aiogram.types.InlineKeyboardMarkup(inline_keyboard=KeyBoard)
        await callback.message.answer_photo(photo=self.cladphoto , caption=self.text.order, reply_markup=keyboard)

    async def ProductList(self, callback: aiogram.types.CallbackQuery):
        KeyBoard = [
            [aiogram.types.InlineKeyboardButton(text="🎄 Бошки WhiteWidow [1 - 2600 руб]", callback_data="product_WhiteWidow1")],
            [aiogram.types.InlineKeyboardButton(text="🎄 Бошки WhiteWidow [2 - 3760 руб]", callback_data="product_WhiteWidow2")],
            [aiogram.types.InlineKeyboardButton(text="🎄 Шишки AMNESIA HAZE [1 - 4800 руб]", callback_data="product_AMNESIA1")],
            [aiogram.types.InlineKeyboardButton(text="🍪 Гашиш Изолятор [2г - 3500 руб]", callback_data="product_Issol2")],
            [aiogram.types.InlineKeyboardButton(text="🍪 Гашиш EURO [3г - 5300 руб]", callback_data="product_EURO3")],
            [aiogram.types.InlineKeyboardButton(text="🧂 a-PVP/CK Белый Кристалл [0.5г - 1530 руб]", callback_data="product_PVP05")],
            [aiogram.types.InlineKeyboardButton(text="🧂 a-PVP/CK Белый Кристалл [1г - 2730 руб]", callback_data="product_PVP1")],
            [aiogram.types.InlineKeyboardButton(text="🧂 a-PVP/CK Белый Кристалл [2г - 3530 руб]", callback_data="product_PVP2")],
            [aiogram.types.InlineKeyboardButton(text="🧊 Амфетамин (VHQ) [1г - 1830 руб]", callback_data="product_AMF1")],
            [aiogram.types.InlineKeyboardButton(text="🧊 Амфетамин (VHQ) [2г - 3000 руб]", callback_data="product_AMF2")],
            [aiogram.types.InlineKeyboardButton(text="🍯 Меф Кристалл VHQ [0.5г - 1580 руб]", callback_data="product_MEF05")],
            [aiogram.types.InlineKeyboardButton(text="🍯 Меф Кристалл VHQ [1г - 2540 руб]", callback_data="product_MEF1")],
            [aiogram.types.InlineKeyboardButton(text="🍯 Меф Кристалл VHQ [2г - 4640 руб]", callback_data="product_MEF2")],
            [aiogram.types.InlineKeyboardButton(text="Назад", callback_data="backtostart")]
        ]
        keyboard = aiogram.types.InlineKeyboardMarkup(inline_keyboard=KeyBoard)
        await callback.message.answer_photo(photo=self.cladphoto , caption=self.text.product, reply_markup=keyboard)

    async def Information(self, callback: aiogram.types.CallbackQuery):
        KeyBoard = [
            [aiogram.types.InlineKeyboardButton(text="Назад", callback_data="backtostart")]
        ]
        keyboard = aiogram.types.InlineKeyboardMarkup(inline_keyboard=KeyBoard)
        await callback.message.answer_photo(photo=self.cladphoto , caption=self.text.informatio, reply_markup=keyboard)

    async def ProductHandler(self, callback: aiogram.types.CallbackQuery):

        text = f"""❗PVP777❗
Фасовка: {self.product.get(callback.data.split("_")[1]).get("Doze")}
Цена: {self.product.get(callback.data.split("_")[1]).get("Price")}

Описание товара:
{self.product.get(callback.data.split("_")[1]).get("Descript")}"""
        KeyBoard = [
            [aiogram.types.InlineKeyboardButton(text="Назад", callback_data="backtoproduct"),
             aiogram.types.InlineKeyboardButton(text="✅ Сделать заказ", callback_data=f"buy_{self.product.get(callback.data.split("_")[1]).get("Price")}")]
        ]
        keyboard = aiogram.types.InlineKeyboardMarkup(inline_keyboard=KeyBoard)

        await callback.message.answer_photo(photo=self.product.get(callback.data.split("_")[1]).get("imagepath"), caption=text, reply_markup=keyboard)

    async def BuyProduct(self, callback: aiogram.types.CallbackQuery):
        price = int(callback.data.split("_")[1])
        KeyBoard = [
            [aiogram.types.InlineKeyboardButton(text="Оплатить", url=self.payer.GeneratePaymentLink(price=price, message=callback.message))]
        ]
        keyboard = aiogram.types.InlineKeyboardMarkup(inline_keyboard=KeyBoard)
        await callback.message.answer(text=f"Ожидаем оплаты: {price} р", reply_markup=keyboard)

