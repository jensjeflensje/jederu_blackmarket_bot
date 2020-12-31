def check(author):
    def inner_check(reaction, user):
        return user == author and reaction.emoji == "✅"
    return inner_check
