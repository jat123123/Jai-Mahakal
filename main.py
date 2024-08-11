from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager,Screen
from kivymd.uix.card import MDCard
from kivymd.uix.label import MDLabel
import webbrowser
from kivymd.toast.kivytoast.kivytoast import toast

kv='''

#:import w kivy.uix.effectwidget
Manager:
    Fir:
    Sec:        
        
<Fir>:
    name:'sc1'    
  
        
    MDBottomNavigation:
        id:bn1
        pos_hint:{'bottom':1}
        panel_color:0,1,0,1
        text_color_active:1,0,1,1
        text_color_normal:0,0,0,1
        MDBottomNavigationItem:
            name:'s1'
            icon:'home'
            text:'Home'
            Carousel:
                direction:'bottom'
                MDCard:
                    id:m1
                    elevation:99999
                    orientation:'vertical'                        
                        
                      
                MDCard:
                    id:m2                              
                   
                 
                 
                    
          
      
                      
                                                                  
        MDBottomNavigationItem:
            name:'s2'
            id:s2
            icon:'language-python'
            text:'Python'    
            Carousel:
                id:c2
               
                
                        

    MDTopAppBar:
        md_bg_color:0,1,0,1
        pos_hint:{'top':1}
        title:'JAI MAHAKAL'
        left_action_items:[['menu',lambda x:nd1.set_state('open')]]
    
    MDNavigationDrawer:
        id:nd1      
        MDList:
            pos_hint:{'center_y':0.96}     
                                
            OneLineIconListItem:
                text:'YouTube'             
                font_size:'10sp'
                on_press:
                    app.pr()
                IconLeftWidget:
                    icon:'youtube'
                    md_bg_color:'red'
                    on_press:
                        app.pre()
          



'''





class Sec(Screen):
    pass




class Fir(Screen):
    pass
    
    
    

class Manager(ScreenManager):
    pass




class demo(MDApp):
    def build(self):
        self.theme_cls.theme_style='Light'
        self.bu=Builder.load_string(kv)
        return self.bu
        
    def pr(self):
        try:
            webbrowser.open('https://youtube.com/shorts/kKQv_wpl4vM?si=-IoSsnTSEPsOLMJ8')                
        except:
            toast('INTERNET ERROR')                                            
    def pre(self):
        try:
            webbrowser.open('https://youtube.com/@ffgaming-su2eu?si=8tcHx5GO39kSv0sO')           
        except:
            toast('INTERNET ERROR')                              
        
        
        
demo().run()
        