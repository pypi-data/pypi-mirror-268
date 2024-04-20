import customtkinter as ctk
from PIL import Image, ImageTk
import numpy as np
from .Theme import *
from .utils import hvr_clr_g
import textwrap

class C_Widgits():
    def __init__(self, page_class, parent):
        self.page = page_class
        self.parent = parent
        self.c = 1 # multiplier for y padding
        
    def section(self, Title=None, padx=0, pady=10, button_text=None, button_command=None, button_icon=None, icon_height=50):
        section_frame = ctk.CTkFrame(self.parent, fg_color= "transparent")

        if Title != "" and Title != None:
            title_frame = ctk.CTkFrame(section_frame, fg_color= "transparent")
            section_label = ctk.CTkLabel(title_frame, text=f"{Title}", font=(FONT_B, 25), fg_color="transparent", text_color=(LIGHT_MODE["text"], DARK_MODE["text"]), anchor="w")
            section_label.pack(side="left", fill="x", padx=20)
            title_frame.pack(fill="x")

        if button_text != None:
            if button_icon != None:
                button_icon = Image.open(button_icon)
                w, h = button_icon.size[0],button_icon.size[1]
                r = w/h
                s = (int(icon_height*r), int(icon_height))
                button_icon = ctk.CTkImage(button_icon, size=s)
            section_button = ctk.CTkButton(title_frame, text=f"{button_text}", font=(FONT, 15), command=button_command, fg_color=(LIGHT_MODE["accent"], DARK_MODE["accent"]), hover_color=(hvr_clr_g(LIGHT_MODE["accent"], "l", 20), hvr_clr_g(DARK_MODE["accent"], "d", 20)), image=button_icon)
            section_button.pack(side="right", fill="x", padx=20)
        

        ops_frame = ctk.CTkFrame(section_frame, fg_color= "transparent")
        ops_frame.pack(fill="x", padx=20, pady=10)

        section_frame.pack(fill="x", padx=padx, pady=pady)

        if button_text==None:
            return ops_frame  
        else:
            return ops_frame, section_button
    
###############################################################################################################################################################################################

    def section_unit(self, section, title : str = "", widget : str =None, command: callable =None, values : list =None, default : str =None):
        """
        Adds a unit to a section with specified parameters.

        Parameters:
        - section (ctk.Frame): The parent widget to which the unit will be added.
        - title (str, optional): The title of the unit.
        - widget (str, optional): The type of widget to be used in the unit. 
            - Supported values: "combobox", "button", "checkbox", "entry", "switch".
        - command (callable, optional): The command to be executed when the widget is interacted with.
        - values (list, optional): A list of values to populate a combobox widget.
        - default: The default value for the widget.
            - treated as the text for a button widget.

        Returns:
        - ctk.Frame: The frame containing the unit.

        You can get the value of the widget using the gval method of the returned frame.
        """
                
        unit_parent = section
        unit_frame = ctk.CTkFrame(unit_parent, fg_color= "transparent")

        unit_label = ctk.CTkLabel(unit_frame, text=f"{title}", font=(FONT, 20))
        unit_label.pack(side="left", fill="x", padx=20, pady=10)

        if widget == "combobox" or widget == "ComboBox":
            unit_option = ctk.CTkComboBox(unit_frame, font=(FONT, 15), values = values, dropdown_font=(FONT, 15), state="readonly", command=command)
            unit_option.set(f"{default}")
            unit_option.pack(side="right", fill="x", padx=20, pady=10)

        if widget == "button" or widget == "Button":
            unit_option = ctk.CTkButton(unit_frame, text=f"{'' if default == None else default}", font=(FONT, 15), command=command, fg_color=(LIGHT_MODE["accent"], DARK_MODE["accent"]), hover_color=(hvr_clr_g(LIGHT_MODE["accent"], "l", 20), hvr_clr_g(DARK_MODE["accent"], "d", 20)))
            unit_option.pack(side="right", fill="x", padx=20, pady=10)

        if widget == "checkbox" or widget == "CheckBox":
            unit_option = ctk.CTkCheckBox(unit_frame, text="", command=command, fg_color=(LIGHT_MODE["accent"], DARK_MODE["accent"]), hover_color=(hvr_clr_g(LIGHT_MODE["accent"], "l", 20), hvr_clr_g(DARK_MODE["accent"], "d", 20)), onvalue=True, offvalue=False,)
            if default != None:
                unit_option.configure(variable=default) 
            unit_option.pack(side="right", fill="x", pady=10)

        if widget == "entry" or widget == "Entry":
            unit_option = ctk.CTkEntry(unit_frame, font=(FONT, 15), fg_color="transparent", placeholder_text=f"{default}", placeholder_text_color=(LIGHT_MODE["text"], DARK_MODE["text"]))
            # unit_option.insert(0, f"{default}")
            unit_option.pack(side="right", fill="x", padx=20, pady=10)

        if widget == "switch" or widget == "Switch":
            unit_option = ctk.CTkSwitch(unit_frame, command=command, fg_color=(hvr_clr_g(LIGHT_MODE["background"], "l", 85), hvr_clr_g(DARK_MODE["background"], "d", 85)), progress_color=(LIGHT_MODE["accent"], DARK_MODE["accent"]), onvalue=True, offvalue=False, text="", bg_color="transparent", border_color="transparent")
            if default != None:
                unit_option.configure(variable=default) 
            unit_option.pack(side="right", fill="x", pady=10)

        unit_frame.pack(fill="x")

        def gval():
            if widget != None:
                return unit_option.get()
            return None
        unit_frame.gval = gval

        self.page.called_when_opened()
        
        return unit_frame
    
###############################################################################################################################################################################################

    def add_tab(self, section, text=None, image=None, size=None, image_size=250): # (frame >> frame_template, image input is of a normal image)
        if image != None:        
            im = Image.open(image)
            w, h = im.size[0],im.size[1]
            r = w/h
            s = (image_size, int(image_size/r))
            im_ctk = ctk.CTkImage(im, size=s)
                    
        if size == "l":
            self.large(section, text, im_ctk)
        elif size == "s":
            self.small(section, text, im_ctk)
        
        self.page.called_when_opened()

    # Type num 1 (Ready to use)
    def Label_func(self, parent_f):          
        l_widget = ctk.CTkLabel(parent_f, text="No Recent projects", font=(FONT, 20), fg_color="transparent", text_color=(LIGHT_MODE["text"], DARK_MODE["text"]), anchor="center")
        l_widget.pack(fill="x", padx=20, pady=10*self.c, expand=True)

    # Type num 2 (Not done yet)
    def large(self, parent_f, text, image):  
        tab_cont = ctk.CTkFrame(parent_f, fg_color="transparent", height=300, width=self.parent.winfo_width())

        tabs_f = ctk.CTkButton(tab_cont, fg_color=(LIGHT_MODE["primary"], DARK_MODE["primary"]), height=400, width=350, 
                               text=f"{text}", image=image, compound="top", )
        tabs_f.pack(padx=20, pady=10*self.c)
        
        tab_cont.pack(expand=True, fill="both")

    # Type num 3 (Ready to use)
    def small(self, parent_f, text, image):  
        tab_cont = ctk.CTkFrame(parent_f, fg_color="transparent", height=300, width=self.parent.winfo_width())

        tab_img = ctk.CTkButton(tab_cont, fg_color="transparent", text="", image=image, hover_color=(hvr_clr_g(LIGHT_MODE["background"], "l"), hvr_clr_g(DARK_MODE["background"], "d")))
        tab_img.pack(padx=20, pady=10*self.c, side="left")

        tab_cont.update()
        tit_f   = ctk.CTkFrame(tab_cont, fg_color="transparent",)
        newtext = textwrap.shorten(text, 50)
        tab_tit = ctk.CTkLabel(tit_f, fg_color="transparent", text=f"{newtext}", font=(FONT, 20), anchor="w")
        tab_tit.pack(fill = "both", expand = True)
        tit_f.pack(pady=10*self.c, fill = "x", expand = True, side="left")

        add_btn = ctk.CTkButton(tab_cont, width=30, height=30, text="+", font=(FONT_B, 30),  
                                fg_color=(LIGHT_MODE["accent"], DARK_MODE["accent"]), 
                                hover_color=(hvr_clr_g(LIGHT_MODE["accent"], "l", 20), hvr_clr_g(DARK_MODE["accent"], "d", 20)), 
                                command= lambda : None)                 # command= lambda num = self.image_count.queue[0]: self.add_image_btn_command(num) #
        add_btn.place(relx=0.975, rely=0.5, anchor="e")

        tab_cont.pack(expand=True, fill="both", pady=10)

        White_line = ctk.CTkFrame(parent_f, fg_color=(DARK_MODE["background"], LIGHT_MODE["background"]), height=2)
        White_line.pack(fill="x", expand=True, padx = 20)


class Banner(ctk.CTkFrame):
    def __init__(self, page, parent, overlay_color, image_path=None, banner_title="", banner_content=None, button_text="Click", font=(FONT_B, 25), font2=(FONT, 15), button_command=None, button_colors=(LIGHT_MODE["accent"], DARK_MODE["accent"]), shifter=0, overlay=0.5): 
        #shifter and overlay are values between 0 and 1
        super().__init__(parent, fg_color="transparent")
        if overlay_color == "transparent":
            raise ValueError("Banner color can't be transparent, provide a color value.")
        
        self.page = page
        self.parent_frame = parent
        self.canvas_color = overlay_color

        self.pack(fill="both")
        self.im = Image.open(r"C:\Users\Morad\Desktop\Page_layout_library\Assets\Images\val.png") if image_path is None else Image.open(image_path)
        self.im = self.im.convert("RGBA")
        img_data = np.array(self.im)
        width, _ = self.im.size
        alpha_gradient = np.linspace(30, 255, int(width*overlay), dtype=np.uint8)  # Create a gradient from 255 to 0
        img_data[:, :int(width*overlay), 3] = alpha_gradient  # Assign the gradient to the alpha channel
        self.new_img = Image.fromarray(img_data)
        self.im_tk  = ImageTk.PhotoImage(self.new_img)

        self.banner_ttitle = banner_title
        self.banner_content = banner_content
        self.button_text = button_text
        self.font = font
        self.font2 = font2
        self.shifter = shifter
        
        self.padding = self.font[1]
        self.multi = 1.5

        self.canvas = ctk.CTkCanvas(self, bg=self.canvas_color, bd=0, highlightthickness=0, relief='ridge')
        self.canvas.pack()

        self.action_button = ctk.CTkButton(self, text=self.button_text, command=button_command, fg_color=button_colors, hover_color=(hvr_clr_g(button_colors[0], "l"), hvr_clr_g(button_colors[1], "d")), font=(font[0], font[1]*0.75), corner_radius=0)

        #// self.update_widget()

    def update_widget(self):
        self.update()
        self.frame_width = self.parent_frame.winfo_width()
        if self.frame_width == 1:
            raise ValueError("Parent width is 1, if you're using this widget in a page, make sure it's called when the page is opened.")
        if self.frame_width != self.im_tk.width():
            self.r = self.im.size[0]/self.im.size[1] # aspect ratio = width/height
            self.s = (self.frame_width, int(self.frame_width/self.r))
            self.im_tk  = ImageTk.PhotoImage(self.new_img.resize(self.s))

            try:
                self.canvas.delete("banner_image")
                self.canvas.delete("banner_text")
                self.canvas.delete("banner_content")
            except:
                pass
            self.canvas.config(width=self.s[0], height=self.s[1])
            b_image = self.canvas.create_image(0, 0, anchor="nw", tags="banner_image", image=self.im_tk, )

            #TODO//: wrap all these widgets to a location manager
            #TODO//: use text wrap for dynamic resizing of the banner content
            #TODO: change font size dynamically
            b_titletext = self.canvas.create_text ((self.s[0]*(1/4)*(1/4)), 0, anchor="nw", tags="banner_text" , text=self.banner_ttitle, font=self.font, fill="white")
            bbox_title = self.canvas.bbox(b_titletext)

            if self.banner_content is not None:
                self.numOfChars = 40
                self.banner_content = textwrap.fill(self.banner_content, width=(self.numOfChars/697)*(self.s[0]//2)) # 40 characters per line, 697 is the width available for the text 
                b_content = self.canvas.create_text ((self.s[0]*(1/4)*(1/4)), bbox_title[3]+self.padding, anchor="nw", tags="banner_content" , text=self.banner_content, font=self.font2, fill="white")
                bbox_content = self.canvas.bbox(b_content)
                self.multi = 2
            else:
                bbox_content = bbox_title

            b_btn = self.canvas.create_window ((self.s[0]*(1/4)*(1/4)), bbox_content[3]+(self.multi*self.padding), anchor="nw", tags="acbtn", window=self.action_button)
            bbox_btn = self.canvas.bbox(b_btn)

            length = bbox_btn[3]
            start_y_pos = (self.s[1]-length)/2 + (self.shifter*((self.s[1]-length)/2))
            self.canvas.moveto(b_titletext, (self.s[0]*(1/4)*(1/4)), start_y_pos)
            if self.banner_content is not None:
                self.canvas.moveto(b_content  , (self.s[0]*(1/4)*(1/4)), start_y_pos + bbox_title[3]+self.padding)
            self.canvas.moveto(b_btn      , (self.s[0]*(1/4)*(1/4)), start_y_pos + bbox_content[3]+(self.multi*self.padding))

            self.page.called_when_opened()

        