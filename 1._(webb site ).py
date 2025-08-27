# # # Nicegui
# # # Website
# # # - Frontend:display screen : it uses java scrivt 
# # # - Backend :hidden screen  : fast API

# # # from nicegui import ui

# # # #############
# # # ## CONFIGS ##
# # # #############

# # # ui.colors(
# # #     primary = '#000000'
# # # )

# # # ui.add_css('''
# # # body{
# # #     background: #13FF35
# # # }
# # # ''')


# # # ###############
# # # ## FUNCTIONS ##
# # # ###############

# # # def about():
# # #     dialog.open()

# # # dialog = ui.dialog()
# # # with dialog , ui.card():
# # #     ui.label("this is dialog")

# # # ############ 
# # # ## HEADER ##
# # # ############

# # # with ui.header():
# # #     ui.label("nice") . classes("text-2xl font-bold") 
# # #     ui.space()
# # #     ui.button("about" , on_click=about)
# # #     ui.button(icon="question_mark")
# # #     ui.button("browser")

# # # ##################
# # # ## HERO SECTION ##
# # # ##################

# # # with ui.image(e:\Ab Zia\ab picks\IMG_5079[1].JPG) . classes('w-full h-fit'):

# # #     with ui.column() . classes('w-full  h-full  items-center  justify-center'):
# # #         with ui.row() . classes('w-full  p-0'):
# # #             ui.label("Nice Web") . classes('text-6xl  font-mono  m-0')
# # #             ui.label(".com") . classes('text-xl  mt-4  font-mono  m-0')
# # #         ui.label('Nice Web - it is with created with nicegui') . classes('text-2xl  font-mono ')


# # # ui.run(title='Nice Web')





# # ###########################################################

from nicegui import ui

#############
## CONFIGS ##
#############

ui.colors(
    primary='#000000'
)

ui.add_css('''
body {
    background: #13FF35;
}
''')

###############
## FUNCTIONS ##
###############

def about():
    dialog.open()

dialog = ui.dialog()
with dialog:
    with ui.card():
        ui.label("This is dialog")

############ 
## HEADER ##
############

with ui.header():
    ui.label("nice").classes("text-2xl font-bold")
    ui.space()
    ui.button("About", on_click=about)
    ui.button(icon="question_mark")
    ui.button("Browser")

##################
## HERO SECTION ##
##################

# ✅ Method 1: Direct image (no overlay)
ui.add_css('''
    .hero {
        background-image: url("e:/Ab Zia/ab picks/IMG_5079[1].JPG");
        background-size: cover;
        background-position: center;
    }
''')

# ✅ Method 2: Background image with overlay text
with ui.image('https://media.istockphoto.com/id/517188688/photo/mountain-landscape.jpg?s=612x612&w=0&k=20&c=A63koPKaCyIwQWOTFBRWXj_PwCrR4cEoOw2S9Q7yVl8='
            ).classes('w-full h-fit items-center justify-center'):
    with ui.column().classes('hero w-full h-full items-center justify-center text-white'):
        with ui.row().classes('gap-2'):
            ui.label("Nice Web").classes('text-6xl font-mono m-0')
            ui.label(".com").classes('text-xl mt-4 font-mono m-0')
        ui.label('Nice Web - created with NiceGUI').classes('text-2xl font-mono')

################
## RUN APP #####
################
     
ui.run(title='Nice Web')



# #########################


# from nicegui import ui

# #############
# ## CONFIGS ##
# #############

# ui.colors(primary='#000000')

# ui.add_css('''
# body {
#     background: #13FF35;
# }
# .hero {
#     background-image: url("e:/Ab Zia/ab picks/IMG_5079_1.JPG");
#     background-size: cover;
#     background-position: center;
# }
# ''')

# ###############
# ## FUNCTIONS ##
# ###############

# def about():
#     dialog.open()

# dialog = ui.dialog()
# with dialog:
#     with ui.card():
#         ui.label("This is dialog")

# ############ 
# ## HEADER ##
# ############

# with ui.header():
#     ui.label("nice").classes("text-2xl font-bold")
#     ui.space()
#     ui.button("About", on_click=about)
#     ui.button()
#     ui.run()

############################################################################

# from nicegui import ui

# #############
# ## CONFIGS ##
# #############

# ui.colors(primary='#000000')

# ui.add_css('''
# body {
#     background: #13FF35;
# }
# .hero {
#     background-image: url("e:/Ab Zia/ab picks/IMG_5079_1.JPG");
#     background-size: cover;
#     background-position: center;
# }
# ''')

# ###############
# ## FUNCTIONS ##
# ###############

# def about():
#     dialog.open()

# dialog = ui.dialog()
# with dialog:
#     with ui.card():
#         ui.label("This is dialog")

# ############ 
# ## HEADER ##
# ############

# with ui.header():
#     ui.label("nice").classes("text-2xl font-bold")
#     ui.space()
#     ui.button("About", on_click=about)
#     ui.button(icon="question_mark")
#     ui.button("Browser")

# ##################
# ## HERO SECTION ##
# ##################

# with ui.card().classes('hero w-full h-[80vh] flex items-center justify-center'):
#     with ui.column().classes('items-center justify-center text-white'):
#         with ui.row().classes('p-0'):
#             ui.label("Nice Web").classes('text-6xl font-mono m-0')
#             ui.label(".com").classes('text-xl mt-4 font-mono m-0')
#         ui.label('Nice Web - created with NiceGUI').classes('text-2xl font-mono')

# ################
# ## RUN APP #####
# ################
# ui.run(title='Nice Web')

