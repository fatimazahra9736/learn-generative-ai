users:list[dict] = [
    {
        "name": "eli1",
        "email": "eli1@gmail.com",
    },
    {
        "name": "eli2",
        "email": "eli2@gmail.com",
    },
    {
        "name": "eli3",
        "email": "eli3@gmail.com",
    },
    {
        "name": "eli4",
        "email": "eli4@gmail.com",
    },
    {
        "name": "eli5",
        "email": "eli5@gmail.com",
    },
]

emails:list[str] = [email["email"] for email in users]

print(emails)

