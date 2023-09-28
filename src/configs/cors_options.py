from configs.allowed_origins import allowed_origins

cors_options = {
    "origin": lambda origin, callback: (callback(None, True) if origin in allowed_origins or not origin else callback("Not allowed by CORS.", False)),
    "options_success_status": 200,
}