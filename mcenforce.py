import contentful
import os

allowMinecraft = True

try:
    client = contentful.Client(
        os.environ['CONTENTFUL_SPACE_ID'],  # This is the space ID. A space is like a project folder in Contentful terms
        os.environ['CONTENTFUL_API_KEY']  # This is the access token for this space. Normally you get both ID and the token in the Contentful web app
    )

    allowMinecraft = getattr( client.entry('u31h5cuLjVuSKQKj2cJln'), 'allow_minecraft', False )
except:
    print ("error getting config")
    pass

if (allowMinecraft == False):
    print("Minecraft is not allowed on this mac.")
    os.system( 'kill $(ps aux | grep \'java\' | awk \'{print $2}\')' )
else:
    print('Not doing anything.')

