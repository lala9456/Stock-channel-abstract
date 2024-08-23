from discord_webhook import DiscordWebhook, DiscordEmbed
from dotenv import load_dotenv
import os
load_dotenv()
dc_url = os.environ.get('DC_WEBHOOK')
# webhook = DiscordWebhook(url=dc_url, id="your webhook message id", content="test")
# response = webhook.execute()


def dc_abstract_notify(abstract_text:str,yt_url:str):
    webhook = DiscordWebhook(url=dc_url, username="摘要機器人")
    embed = DiscordEmbed(
        title="DC專用機器人", description="財經節目摘要", color="03b2f8"
    )
    embed.set_author(
        name="老王",
        # url="https://github.com/lovvskillz",
        # icon_url="https://avatars0.githubusercontent.com/u/14542790",
    )
    embed.add_embed_field(name="影片網址", value=yt_url, inline=False)
    embed.add_embed_field(name="節目摘要", value=abstract_text, inline=False)
    webhook.add_embed(embed)
    response = webhook.execute()

if __name__=="__main__":
    dc_abstract_notify(abstract_text="摘要測試",yt_url="https://www.youtube.com/watch?v=dfUe6N4Y9y0&t=67s")




# webhook = DiscordWebhook(url=dc_url, username="New Webhook Username")

# embed = DiscordEmbed(
#     title="Embed Title", description="Your Embed Description", color="03b2f8"
# )
# embed.set_author(
#     name="Author Name",
#     url="https://github.com/lovvskillz",
#     icon_url="https://avatars0.githubusercontent.com/u/14542790",
# )
# embed.set_footer(text="Embed Footer Text")
# embed.set_timestamp()
# # Set `inline=False` for the embed field to occupy the whole line
# embed.add_embed_field(name="Field 1", value="Lorem ipsum", inline=False)
# embed.add_embed_field(name="Field 2", value="dolor sit", inline=False)
# embed.add_embed_field(name="Field 3", value="amet consetetur")
# embed.add_embed_field(name="Field 4", value="sadipscing elitr")

# webhook.add_embed(embed)
# response = webhook.execute()