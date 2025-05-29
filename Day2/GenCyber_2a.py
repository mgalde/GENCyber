import os
import zipfile
from datetime import datetime

# Prompt student for phishing email content
student_name = input("Enter your name or codename: ").strip().replace(" ", "_")
victim_name = input("Enter the victim's name (e.g., Mr. Smith): ").strip()
message_body = input("Enter the phishing message (what the email says): ").strip()
phishing_link = input("Enter the fake phishing link (e.g., http://prize-claim.biz): ").strip()

header_image = input("Enter the file path for a HEADER image (or leave blank): ").strip()
center_image = input("Enter the file path for a CENTER image (or leave blank): ").strip()
footer_image = input("Enter the file path for a FOOTER image (or leave blank): ").strip()

# HTML content with fake email client look
html_content = f"""<!DOCTYPE html>
<html>
<head>
    <title>Phishing Email</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            padding: 20px;
        }}
        .email-container {{
            background-color: #ffffff;
            border: 1px solid #cccccc;
            border-radius: 8px;
            max-width: 600px;
            margin: auto;
            padding: 20px;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
        }}
        .header, .center-img, .footer {{
            text-align: center;
            margin: 15px 0;
        }}
        .phish-link {{
            background-color: #007bff;
            color: white;
            padding: 10px 15px;
            text-decoration: none;
            border-radius: 5px;
        }}
        .meta {{
            font-size: 0.85em;
            color: #888;
            margin-bottom: 10px;
        }}
    </style>
</head>
<body>
    <div class="email-container">
        <div class="meta">From: support@schooladmin.org<br>To: {victim_name}<br>Date: {datetime.now().strftime('%B %d, %Y')}</div>
        {'<div class="header"><img src="' + os.path.basename(header_image) + '" width="100%"></div>' if header_image else ''}
        <p>{message_body}</p>
        <p style="text-align:center;">
            <a href="{phishing_link}" class="phish-link">Click here</a>
        </p>
        {'<div class="center-img"><img src="' + os.path.basename(center_image) + '" width="80%"></div>' if center_image else ''}
        {'<div class="footer"><img src="' + os.path.basename(footer_image) + '" width="100%"></div>' if footer_image else ''}
    </div>
</body>
</html>
"""

# Write the HTML file
html_filename = "phish_email.html"
with open(html_filename, "w", encoding="utf-8") as f:
    f.write(html_content)

# Collect files to zip
files_to_zip = [html_filename]
for img in [header_image, center_image, footer_image]:
    if img and os.path.exists(img):
        files_to_zip.append(img)

zip_filename = f"{student_name}_phish.zip"
with zipfile.ZipFile(zip_filename, 'w') as zipf:
    for file in files_to_zip:
        zipf.write(file, os.path.basename(file))

print(f"\n✅ Done! Your phishing email has been saved as '{html_filename}' and zipped as '{zip_filename}'.")
print("Send the .zip file to your instructor for classroom review.")
