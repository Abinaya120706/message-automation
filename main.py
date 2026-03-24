import pandas as pd
from twilio.rest import Client
import time

# 🔐 Replace with your actual credentials
ACCOUNT_SID = "your_account_sid"
AUTH_TOKEN = "your_auth_token"

client = Client(ACCOUNT_SID, AUTH_TOKEN)

# 📂 Read Excel file
df = pd.read_excel("data.xlsx")

# 💬 Message templates
messages = {
    'staff': "Good morning sir",
    'friend': "Hi dude!",
    'student': "Study well",
    'sister': "Hey sis!"
}

# 🚀 Loop through data
for i in range(len(df)):
    try:
        name = str(df.loc[i, "designation"]).strip().lower()
        number = str(df.loc[i, "number"]).strip()

        # Format number
        number = "+91" + number

        # Get message
        msg = messages.get(name, "Hello!")

        final_message = f"Dear {name.capitalize()}, {msg}"

        # 📲 Send WhatsApp message
        client.messages.create(
            from_='whatsapp:+14155238886',
            body=final_message,
            to=f'whatsapp:{number}'
        )

        print(f"✅ Sent to {name} -> {number}")

        time.sleep(1)

    except Exception as e:
        print(f"❌ Error sending to row {i}: {e}")
