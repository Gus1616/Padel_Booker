import schedule
import time
import padel_booker

def book_slots():
    # Call your booking bot's main function here
    print("Booking slots...")
    padel_booker.booker()

# Schedule the bot to run every 2 weeks on Wednesday at 8 PM
schedule.every(2).weeks.on('Wednesday').at("20:00").do(book_slots)


while True:
    schedule.run_pending()
    time.sleep(1)