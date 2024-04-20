def get_filename_from_api(response, default_filename="defaultFie"):
    content_disposition = response.headers.get('Content-Disposition')
    if content_disposition:
        return content_disposition.split("filename=")[1].split(";")[0].replace("\"", "")
    return default_filename
