from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "8342783818:AAEna2YS62d3vADpKmCWZrja7uttjEdcGvk"  # Reemplaza con tu token de BotFather

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Mensaje de bienvenida
    mensaje = (
        "👋 *¡Hola! Soy tu asistente virtual de CNT*\n\n"
        "Estoy aquí para ayudarte a acceder rápidamente a los servicios más consultados 📡✨\n\n"
        "Por favor, selecciona la opción que deseas consultar:"
    )

    # Crear los botones estilo menú con emojis
    keyboard = [
        [InlineKeyboardButton("🏢 Página principal CNT", url="https://micnt.com.ec:8443/web/index.php")],
        [InlineKeyboardButton("🎁 Promociones CNT", url="https://cnt.com.ec/promociones")],
        [InlineKeyboardButton("🛠 Servicios en línea CNT", url="https://cnt.com.ec/paginas/servicios-en-linea")],
        [InlineKeyboardButton("📞 Atención Soporte CNT", url="https://cntinternetchateaconnosotros.cnt.gob.ec:8054/internet/")],
        [InlineKeyboardButton("🌐 Planes de Internet CNT", url="https://cnt.com.ec/productos/planes-internet/")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    # Enviar mensaje con botones
    await update.message.reply_text(mensaje, reply_markup=reply_markup, parse_mode="Markdown")

if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    print("🤖 Bot CNT en ejecución...")
    app.run_polling()

