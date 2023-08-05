from bot_function.service import Service
import message_text


class ChekMessage(Service):
    """Отправляем задание и проверяем код."""
    def send_msg(self, message, quest):
        """Отправляет сообщение"""
        if quest != 5:
            self.bot.send_message(message.chat.id, message_text.MSG_DICT[str(quest+1)])
            self.bot.register_next_step_handler(message, self.chek_code, quest)
        else:
            self.bot.send_message(message.chat.id, """Сложи всё вместе и напиши ответ в чат
У тебя 3 попытки!""")
            self.bot.register_next_step_handler(message, self.chek_exit)

    def chek_code(self, message, quest):
        """Проверяем отправленный код."""
        if message.text.lower() == message_text.CODE_DICT[str(quest+1)]:
            self.bot.send_message(message.chat.id, "Верно, ты молодец!")
            quest += 1
            self.send_msg(message, quest)
        else:
            self.bot.send_message(message.chat.id, "Кажется ответ другой, давай ещё раз")
            self.bot.register_next_step_handler(message, self.chek_code, quest)

    def chek_exit(self, message):
        """Проверяем заключительный код."""
        if message.text.lower() == 'подарок в рюкзаке':
            self.bot.send_message(message.chat.id, 'Молодец, у тебя 3 попытки, 1 рюкзак - 1 попытка')
        else:
            self.bot.send_message(message.chat.id, 'Не верно, давай ещё раз')
