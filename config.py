import os
from datetime import datetime

# --- Bot Credentials ---
API_ID = 39005479
API_HASH = "c2e7265b2e96025adcc4731c2c1e5ba5"
BOT_TOKEN = "8534739129:AAEY1_SiskC73NPMBq3IDU8XfYCbVuZWbsE"
SESSION_STRING = "BQJTLScAnOFYKCwnyrSjEUcnuqVN7bm85oVmteMpak2s4XL7Hb0yQ04kwaMAMtPZqSUUJaCr97887jGaR8LlEX8zocmr5Mutz7tXGOKUnCDNWxX1KHvkbRczcdMaQHFHFxO1mxCvdOx8abVkTpcV5IyTnlO6GO6IwFiISPYTRF3ekCiZFWhYC0oH3ZzFRMVXtSAMFH8G1rxKwkmn_ooOXNJZdoTNfMzv4_WU_Jusp8ASALGU3WV30Ugn8UEtYm2glTo0V9nuOGv_ZF7zQA-trkQjRnKM17JGTxDFVvk9LZSF03ekSV7cAdje4dJM_XVHwyewU3cRX4zzfpE3CJ3e_jqQG0iKDwAAAAIKSZQTAA"
# --- Random image links ---" # Apni session string yahan puri daal dena
OWNER_ID = 7724452546
# --- Global Tracking ---
queues = {}
playing_messages = {} # {chat_id: message_id} - Timer edit karne ke liye
current_playing = {} # {chat_id: song_details} - Currently playing track ke liye
BOT_START_TIME = datetime.now()
