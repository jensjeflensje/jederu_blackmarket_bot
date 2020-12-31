from checks import check
import tokens as check_tokens


async def execute_action_for_tokens(ctx, client, action, args, tokens):
    current_tokens = check_tokens.get_tokens(ctx.author.id)
    if current_tokens < tokens:
        await ctx.send(f"Sorry man, je hebt te weinig tokens")
        return
    msg = await ctx.send(f"Klik op het vinkje om je betaling van {tokens} tokens toe te staan.")
    await msg.add_reaction("✅")
    await client.wait_for('reaction_add', check=check(ctx.author), timeout=300)
    check_tokens.subtract_tokens(ctx.author.id, tokens)
    await ctx.send("Actie uitgevoerd.")
    await action(*args)

