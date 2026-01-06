from flask import Flask, request, jsonify
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)

otp_store = {}

@app.route("/send-otp", methods=["POST"])
def send_otp():
    phone = request.json.get("phone")

    otp = str(random.randint(100000, 999999))
    otp_store[phone] = otp

    # OTP shown in terminal for demo
    print(f"[DEMO OTP] Phone: {phone}, OTP: {otp}")

    return jsonify({
        "success": True,
        "otp": otp  # returned ONLY for demo
    })

@app.route("/verify-otp", methods=["POST"])
def verify_otp():
    phone = request.json.get("phone")
    otp = request.json.get("otp")

    if otp_store.get(phone) == otp:
        return jsonify({"success": True})
    return jsonify({"success": False})

if __name__ == "__main__":
    app.run(debug=True)
