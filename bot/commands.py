# from telegram import Update
# from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
# # import outcalc

def print_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message.text
    print(msg)
    items = msg.split()
    x = items[1]
    y = items[2]
    z = items[3]
    update.message.reply_text(f'{x} + {y} = {z} ')

# def sum_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     msg = update.message.text
#     print(msg)
#     items = msg.split()
#     x = int(items[1])
#     y = int(items[2])
#     z = items[3]
#     outcalc.myOutput(x,y,z)
#     update.message.reply_text(f'{x} + {y} = {x+y} ')

# async def min_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     msg = update.message.text
#     print(msg)
#     items = msg.split()
#     x = int(items[1])
#     y = int(items[2])
#     await update.message.reply_text(f'{x} - {y} = {x-y} ')