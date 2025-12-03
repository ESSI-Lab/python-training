def obfuscate_token(url, token):
    """
    Replace the token in a URL with '***' for safe printing.
    """
    return url.replace(token, "***")
