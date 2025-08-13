import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import pytesseract
from PIL import Image
import io

# Load environment variables
load_dotenv()

# Configure pytesseract
pytesseract.pytesseract.tesseract_cmd = os.getenv('TESSERACT_CMD')

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Send a message when the command /start is issued."""
    await update.message.reply_text(
        'Hi! Send me an image with text, and I will extract the text for you.'
    )

async def extract_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Extract text from the received image."""
    # Check if the message contains a photo
    if not update.message.photo:
        await update.message.reply_text("Please send an image with text.")
        return
    
    try:
        # Get the highest resolution photo
        photo_file = await update.message.photo[-1].get_file()
        
        # Download the photo to memory
        photo_bytes = await photo_file.download_as_bytearray()
        
        # Open the image with PIL
        image = Image.open(io.BytesIO(photo_bytes))
        
        # Extract text using pytesseract
        text = pytesseract.image_to_string(image)
        
        if text.strip():
            await update.message.reply_text(f"Extracted text:\n\n{text}")
        else:
            await update.message.reply_text("No text found in the image.")
            
    except Exception as e:
        await update.message.reply_text(f"An error occurred: {str(e)}")

def main():
    """Start the bot."""
    # Create the Application
    application = Application.builder().token(os.getenv('TELEGRAM_BOT_TOKEN')).build()

    # Add handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.PHOTO, extract_text))
    
    # Run the bot
    application.run_polling()

if __name__ == "__main__":
    main()