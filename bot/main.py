from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler
import calc


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')

async def print_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message.text
    print(msg)
    items = msg.split()
    num1 = items[1]
    num2 = items[3]
    oper = items[2]
    result = calc.op1(num1,num2,oper)
    print(result)
    await update.message.reply_text(f'{num1} {oper} {num2} = {result}')
    # resalt = calc.calculate(num1,num2)


app = ApplicationBuilder().token("5767301439:AAH_QKX_dM6mSbNMQBVL7PbmMsDD_ECoFoA").build()

app.add_handler(CommandHandler("hello", hello))
app.add_handler(CommandHandler('calc',print_command))
# app.add_handler(CommandHandler("min", commands.min_command))
print('Start server')
app.run_polling()

# async def sum_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     msg = update.message.text
#     print(msg)
#     items = msg.split()
#     x = int(items[1])
#     y = int(items[2])
#     await update.message.reply_text(f'{x} + {y} = {x+y} ')

# async def min_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     msg = update.message.text
#     print(msg)
#     items = msg.split()
#     x = int(items[1])
#     y = int(items[2])
#     await update.message.reply_text(f'{x} + {y} = {x+y} ')

