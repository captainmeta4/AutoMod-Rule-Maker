from tkinter import *
import webbrowser
import random
import functools
import re

#other globals
#there should probably be more of these
VERSION="1.1"

class Application():

    def __init__(self):

        self.create_main_window()

    def create_main_window(self):

        #build the main applicationwindow
        self.top = Tk()

        #dictionary of enabled items
        self.values={
            "type":StringVar(),
            "domain_bool":IntVar(),
            "domain_regex_bool":IntVar(),
            "domain_invert":IntVar(),
            "title_bool":IntVar(),
            "title_regex_bool":IntVar(),
            "title_invert":IntVar(),
            "title_case_bool":IntVar(),
            "title_mod":StringVar(),
            "body_bool":IntVar(),
            "body_regex_bool":IntVar(),
            "body_invert":IntVar(),
            "body_case_bool":IntVar(),
            "body_mod":StringVar(),
            "name_bool":IntVar(),
            "name_regex_bool":IntVar(),
            "name_invert":IntVar(),
            "name_mod":StringVar(),
            "c_karma_bool":IntVar(),
            "c_karma_mod":StringVar(),
            "c_karma":StringVar(),
            "l_karma_bool":IntVar(),
            "l_karma_mod":StringVar(),
            "l_karma": StringVar(),
            "t_karma_bool":IntVar(),
            "t_karma_mod":StringVar(),
            "t_karma":StringVar(),
            "age_bool":IntVar(),
            "age_mod":StringVar(),
            "age":StringVar(),
            "moderate_bool":IntVar(),
            "moderate_action":StringVar(),
            "reason_text":StringVar(),
            "comment_bool":IntVar(),
            "modmail_bool":IntVar(),
            "message_bool":IntVar(),
            "rule_name":StringVar()
            }
        
        #build the criteria items
        criteria_frame=LabelFrame(master=self.top, text="If the reddit thing matches all this...")
        criteria_frame.grid(row=1,column=0, sticky=NSEW)


        #item type
        type_label=Label(master=criteria_frame, text="Item Type:")
        type_label.grid(row=1,column=0)

        type_frame=Frame(master=criteria_frame)
        type_frame.grid(row=1,column=2)
        
        r1=Radiobutton(master=type_frame, text="All Content", variable=self.values['type'],value="both")
        r2=Radiobutton(master=type_frame, text="Submissions", variable=self.values['type'],value="submission")
        r3=Radiobutton(master=type_frame, text="Link Submissions", variable=self.values['type'],value="link submission")
        r4=Radiobutton(master=type_frame, text="Text Submissions", variable=self.values['type'],value="text submission")
        r5=Radiobutton(master=type_frame, text="Comments", variable=self.values['type'],value="comment")
        r1.pack(anchor=W)
        r2.pack(anchor=W)
        r3.pack(anchor=W)
        r4.pack(anchor=W)
        r5.pack(anchor=W)
        r1.select()


        #domain
        domain_label=Checkbutton(master=criteria_frame, text="Domain:", variable=self.values['domain_bool'])
        domain_label.grid(row=2,column=0)

        domain_mods_frame=Frame(master=criteria_frame)
        domain_mods_frame.grid(row=2,column=1)

        i1=Checkbutton(master=domain_mods_frame,text="regex",variable=self.values['domain_regex_bool'])
        i2=Checkbutton(master=domain_mods_frame,text="inverse",variable=self.values['domain_invert'])
        i1.pack(anchor=W)
        i2.pack(anchor=W)

        self.domain_entry=Text(master=criteria_frame,relief=SUNKEN,height=8,width=20, bg="#ffffff")
        self.domain_entry.grid(row=2,column=2)

        
        #title
        title_label=Checkbutton(master=criteria_frame, text="Title:", variable=self.values['title_bool'])
        title_label.grid(row=3,column=0)

        title_mods_frame=Frame(master=criteria_frame)
        title_mods_frame.grid(row=3,column=1,pady=5)
    
        r12=Checkbutton(master=title_mods_frame, text="regex", variable=self.values['title_regex_bool'])
        i3= Checkbutton(master=title_mods_frame, text="inverse",variable=self.values['title_invert'])
        i5= Checkbutton(master=title_mods_frame, text="case-sensitive",variable=self.values['title_case_bool'])
        r13=Radiobutton(master=title_mods_frame, text="includes-word", variable=self.values['title_mod'], value="includes-word")
        r14=Radiobutton(master=title_mods_frame, text="includes", variable=self.values['title_mod'], value="includes")
        r15=Radiobutton(master=title_mods_frame, text="starts-with", variable=self.values['title_mod'], value="starts-with")
        r16=Radiobutton(master=title_mods_frame, text="ends-with", variable=self.values['title_mod'], value="ends-with")
        r17=Radiobutton(master=title_mods_frame, text="full-exact", variable=self.values['title_mod'], value="full-exact")
        r12.pack(anchor=W)
        i3.pack(anchor=W)
        i5.pack(anchor=W)
        r13.pack(anchor=W)
        r14.pack(anchor=W)
        r15.pack(anchor=W)
        r16.pack(anchor=W)
        r17.pack(anchor=W)
        r13.select()

        self.title_entry=Text(master=criteria_frame,relief=SUNKEN,height=8, width=20,bg="#ffffff")
        self.title_entry.grid(row=3,column=2)

        #body
        body_label=Checkbutton(master=criteria_frame, text="Body:", variable=self.values['body_bool'])
        body_label.grid(row=4,column=0)

        body_mods_frame=Frame(master=criteria_frame)
        body_mods_frame.grid(row=4,column=1,pady=5)
    
        r6=Checkbutton(master=body_mods_frame, text="regex", variable=self.values['body_regex_bool'])
        i4=Checkbutton(master=body_mods_frame, text="inverse",variable=self.values['body_invert'])
        i6= Checkbutton(master=body_mods_frame, text="case-sensitive",variable=self.values['body_case_bool'])
        r7=Radiobutton(master=body_mods_frame, text="includes-word", variable=self.values['body_mod'], value="includes-word")
        r8=Radiobutton(master=body_mods_frame, text="includes", variable=self.values['body_mod'], value="includes")
        r9=Radiobutton(master=body_mods_frame, text="starts-with", variable=self.values['body_mod'], value="starts-with")
        r10=Radiobutton(master=body_mods_frame, text="ends-with", variable=self.values['body_mod'], value="ends-with")
        r11=Radiobutton(master=body_mods_frame, text="full-exact", variable=self.values['body_mod'], value="full-exact")
        r6.pack(anchor=W)
        i4.pack(anchor=W)
        i6.pack(anchor=W)
        r7.pack(anchor=W)
        r8.pack(anchor=W)
        r9.pack(anchor=W)
        r10.pack(anchor=W)
        r11.pack(anchor=W)
        r7.select()


        self.body_entry=Text(master=criteria_frame,relief=SUNKEN,height=8, width=20,bg="#ffffff")
        self.body_entry.grid(row=4,column=2)

        #author criteria

        author_frame=LabelFrame(master=self.top, text="...and the user who posted it matches all this...")
        author_frame.grid(row=1,column=1, sticky=NSEW)   

        #username
        name_label=Checkbutton(master=author_frame, text="Name:", variable=self.values['name_bool'])
        name_label.grid(row=1,column=0)

        name_mods_frame=Frame(master=author_frame)
        name_mods_frame.grid(row=1,column=1,pady=5)
    
        r18=Checkbutton(master=name_mods_frame, text="regex", variable=self.values['name_regex_bool'])
        i7= Checkbutton(master=name_mods_frame, text="inverse",variable=self.values['name_invert'])
        r19=Radiobutton(master=name_mods_frame, text="includes-word", variable=self.values['name_mod'], value="includes-word")
        r20=Radiobutton(master=name_mods_frame, text="includes", variable=self.values['name_mod'], value="includes")
        r21=Radiobutton(master=name_mods_frame, text="starts-with", variable=self.values['name_mod'], value="starts-with")
        r22=Radiobutton(master=name_mods_frame, text="ends-with", variable=self.values['name_mod'], value="ends-with")
        r23=Radiobutton(master=name_mods_frame, text="full-exact", variable=self.values['name_mod'], value="full-exact")
        r18.pack(anchor=W)
        i7.pack(anchor=W)
        r19.pack(anchor=W)
        r20.pack(anchor=W)
        r21.pack(anchor=W)
        r22.pack(anchor=W)
        r23.pack(anchor=W)
        r23.select()

        self.name_entry=Text(master=author_frame,relief=SUNKEN,height=8, width=20,bg="#ffffff")
        self.name_entry.grid(row=1,column=2)

        #comment karma check

        c_karma_label=Checkbutton(master=author_frame, text="Comment Karma:", variable=self.values['c_karma_bool'])
        c_karma_label.grid(row=2,column=0)

        c_karma_mod_frame=Frame(master=author_frame)
        c_karma_mod_frame.grid(row=2,column=1,pady=5)

        r24=Radiobutton(master=c_karma_mod_frame, text=">", variable=self.values['c_karma_mod'], value=">")
        r25=Radiobutton(master=c_karma_mod_frame, text=">=", variable=self.values['c_karma_mod'], value=">=")
        r26=Radiobutton(master=c_karma_mod_frame, text="<", variable=self.values['c_karma_mod'], value="<")
        r27=Radiobutton(master=c_karma_mod_frame, text="<=", variable=self.values['c_karma_mod'], value="<=")
        r24.pack(anchor=W)
        r25.pack(anchor=W)
        r26.pack(anchor=W)
        r27.pack(anchor=W)
        r27.select()

        c_karma_entry=Spinbox(master=author_frame, from_=-100, to=100000, width=7,textvariable=self.values['c_karma'])
        c_karma_entry.grid(row=2,column=2)

        #link karma check

        l_karma_label=Checkbutton(master=author_frame, text="Link Karma:", variable=self.values['l_karma_bool'])
        l_karma_label.grid(row=3,column=0)

        l_karma_mod_frame=Frame(master=author_frame)
        l_karma_mod_frame.grid(row=3,column=1,pady=5)

        r28=Radiobutton(master=l_karma_mod_frame, text=">", variable=self.values['l_karma_mod'], value=">")
        r29=Radiobutton(master=l_karma_mod_frame, text=">=", variable=self.values['l_karma_mod'], value=">=")
        r30=Radiobutton(master=l_karma_mod_frame, text="<", variable=self.values['l_karma_mod'], value="<")
        r31=Radiobutton(master=l_karma_mod_frame, text="<=", variable=self.values['l_karma_mod'], value="<=")
        r28.pack(anchor=W)
        r29.pack(anchor=W)
        r30.pack(anchor=W)
        r31.pack(anchor=W)
        r31.select()

        l_karma_entry=Spinbox(master=author_frame, from_=1, to=100000, width=7,textvariable=self.values['l_karma'])
        l_karma_entry.grid(row=3,column=2)

        #total karma check

        t_karma_label=Checkbutton(master=author_frame, text="Total Karma:", variable=self.values['t_karma_bool'])
        t_karma_label.grid(row=4,column=0)

        t_karma_mod_frame=Frame(master=author_frame)
        t_karma_mod_frame.grid(row=4,column=1,pady=5)

        r32=Radiobutton(master=t_karma_mod_frame, text=">", variable=self.values['t_karma_mod'], value=">")
        r33=Radiobutton(master=t_karma_mod_frame, text=">=", variable=self.values['t_karma_mod'], value=">=")
        r34=Radiobutton(master=t_karma_mod_frame, text="<", variable=self.values['t_karma_mod'], value="<")
        r35=Radiobutton(master=t_karma_mod_frame, text="<=", variable=self.values['t_karma_mod'], value="<=")
        r32.pack(anchor=W)
        r33.pack(anchor=W)
        r34.pack(anchor=W)
        r35.pack(anchor=W)
        r35.select()

        t_karma_entry=Spinbox(master=author_frame, from_=-99, to=100000, width=7,textvariable=self.values['t_karma'])
        t_karma_entry.grid(row=4,column=2)

        #account age check

        age_label=Checkbutton(master=author_frame, text="Account Age (days):", variable=self.values['age_bool'])
        age_label.grid(row=5,column=0)

        age_mod_frame=Frame(master=author_frame)
        age_mod_frame.grid(row=5,column=1,pady=5)

        r36=Radiobutton(master=age_mod_frame, text=">", variable=self.values['age_mod'], value=">")
        r37=Radiobutton(master=age_mod_frame, text=">=", variable=self.values['age_mod'], value=">=")
        r38=Radiobutton(master=age_mod_frame, text="<", variable=self.values['age_mod'], value="<")
        r39=Radiobutton(master=age_mod_frame, text="<=", variable=self.values['age_mod'], value="<=")
        r36.pack(anchor=W)
        r37.pack(anchor=W)
        r38.pack(anchor=W)
        r39.pack(anchor=W)
        r39.select()

        age_entry=Spinbox(master=author_frame, from_=1, to=3650, width=7, textvariable=self.values['age'])
        age_entry.grid(row=5,column=2)

        #actions
        action_frame=LabelFrame(master=self.top, text="...then perform these actions.")
        action_frame.grid(row=1,column=2, sticky=NSEW)

        #moderation action
        moderate_label=Checkbutton(master=action_frame, text="Moderate:", variable=self.values['moderate_bool'])
        moderate_label.grid(row=0,column=0)
        
        moderate_frame=Frame(master=action_frame)
        moderate_frame.grid(row=0,column=2)

        r40=Radiobutton(master=moderate_frame, text="Approve", variable=self.values['moderate_action'],value="approve")
        r41=Radiobutton(master=moderate_frame, text="Remove", variable=self.values['moderate_action'],value="remove")
        r42=Radiobutton(master=moderate_frame, text="Spam", variable=self.values['moderate_action'],value="spam")
        r43=Radiobutton(master=moderate_frame, text="Filter", variable=self.values['moderate_action'],value="filter")
        r44=Radiobutton(master=moderate_frame, text="Report", variable=self.values['moderate_action'],value="report")
        r40.pack(anchor=W)
        r41.pack(anchor=W)
        r42.pack(anchor=W)
        r43.pack(anchor=W)
        r44.pack(anchor=W)
        r41.select()
        
        #reason
        reason_label=Label(master=action_frame,text="Reason:")
        reason_label.grid(row=1,column=0)

        reason_entry=Entry(master=action_frame, textvariable=self.values['reason_text'],width=20)
        reason_entry.grid(row=1,column=2)
        
        #leave comment
        comment_label = Checkbutton(master=action_frame, text="Leave Comment:", variable=self.values['comment_bool'])
        comment_label.grid(row=2,column=0)

        self.comment_entry=Text(master=action_frame,relief=SUNKEN,height=8, width=20,bg="#ffffff")
        self.comment_entry.grid(row=2,column=2)

        #send modmail
        modmail_label = Checkbutton(master=action_frame, text="Send Modmail:", variable=self.values['modmail_bool'])
        modmail_label.grid(row=3,column=0)

        self.modmail_entry=Text(master=action_frame,relief=SUNKEN,height=8, width=20,bg="#ffffff")
        self.modmail_entry.grid(row=3,column=2)

        #send private message
        message_label = Checkbutton(master=action_frame, text="Send Message:", variable=self.values['message_bool'])
        message_label.grid(row=4,column=0)

        self.message_entry=Text(master=action_frame,relief=SUNKEN,height=8, width=20,bg="#ffffff")
        self.message_entry.grid(row=4,column=2)

        #Options
        options_frame = LabelFrame(master=self.top, text="Other Options")
        options_frame.grid(row=0,column=0,columnspan=2, sticky=N+S+E+W)

        #Rule name
        rule_name_label=Label(master=options_frame, text="Rule Name:")
        rule_name_label.grid(row=0,column=0)

        rule_name_entry=Entry(master=options_frame, textvariable=self.values["rule_name"])
        rule_name_entry.grid(row=0,column=1)

        create_rule=Button(master=options_frame, text="Create Rule", command=self.output_text)
        create_rule.grid(row=0,column=2)

        #extras section
        extra_frame=LabelFrame(master=self.top, text="Extras")
        extra_frame.grid(row=0,column=2, sticky=N+E+W+S)

        #about button
        about_button=Button(master=extra_frame, text="About", command=self.about)
        about_button.grid(row=0,column=0)

        #help button
        help_button=Button(master=extra_frame, text="Help", command = self.help)
        help_button.grid(row=0,column=1)

        #send feedback
        feedback_button=Button(master=extra_frame, text="Send Feedback", command=self.feedback)
        feedback_button.grid(row=0,column=2)

        #it took me way to long to realize I needed this line
        self.top.mainloop()

    def help(self):
        url='https://www.reddit.com/r/captainmeta4/wiki/rule_maker_help'
        webbrowser.open(url)

    def feedback(self):

        url="https://www.reddit.com/message/compose/?to=captainmeta4&subject=Feedback%20on%20AutoMod%20Rule%20Generator%20v"+str(VERSION)
        webbrowser.open(url)

    def about(self):

        self.message_box("Version "+str(VERSION)+"\n\ncreated by /u/captainmeta4")

    def message_box(self, text):
        #makes a message box with text
        box=Tk()

        message=Text(master=box)
        message.insert(END, text)
        message.pack()
        message.config(state=DISABLED)
        button=Button(master=box, text="OK", command=box.destroy)
        button.pack()

    def listify(self, text):

        #takes a text block and separates items by newlines or commas into a list

        output = text.split('\n')

        #check for empty final cells

        if output[len(output)-1]=="":
            output.pop()

        return output

    def yamlfy_text(self,text):

        #takes a text block and adds spaces after newlines so that it is good for automod
        #used for comment, modmail, and message commands

        return "        "+text.replace("\n","\n        ")

    def output_text(self):

        #shows a window with automod script
        output_window=Tk()

        output_message=Text(master=output_window)
        output_message.insert(END,self.generate_rule_text())
        output_message.config(state=DISABLED)
        output_message.pack()

        done_button=Button(master=output_window, text="Done",command=output_window.destroy)
        done_button.pack()
         

    def generate_rule_text(self):

        #takes all the input controls and returns a text string that is an AutoMod rule
        #x is a throwaway var used for assembling single lines

        #start with dashes and rule name
        output = "---\n#"+self.values['rule_name'].get()

        #item type
        output +="\n    type: "+self.values['type'].get()

        #domain
        if self.values['domain_bool'].get():
            x="domain"
            if self.values['domain_invert'].get():
                x="~"+x
            if self.values['domain_regex_bool'].get():
                x+=" (regex)"
            x+=": "

            x+=str(self.listify(self.domain_entry.get(1.0,END)))
            x='\n    '+x

            output += x

        #title
        if self.values['title_bool'].get():
            x="title ("
            if self.values['title_invert'].get():
                x="~"+x
            if self.values['title_regex_bool'].get():
                x+="regex, "
            if self.values['title_case_bool'].get():
                x+="case-sensitive, "
            x+=self.values['title_mod'].get()
            x+="): "

            x+=str(self.listify(self.title_entry.get(1.0,END)))
            x='\n    '+x

            output += x

        #body
        if self.values['body_bool'].get():
            x="body ("
            if self.values['body_invert'].get():
                x="~"+x
            if self.values['body_regex_bool'].get():
                x+="regex, "
            if self.values['body_case_bool'].get():
                x+="case-sensitive, "
            x+=self.values['body_mod'].get()
            x+="): "

            x+=str(self.listify(self.body_entry.get(1.0,END)))
            x='\n    '+x

            output += x

        #author conditions

        if (self.values['name_bool'].get()
            or self.values['c_karma_bool'].get()
            or self.values['l_karma_bool'].get()
            or self.values['t_karma_bool'].get()
            or self.values['age_bool'].get()):
            output+="\n    author:"

        #name
        if self.values['name_bool'].get():
            x="name ("
            if self.values['name_invert'].get():
                x="~"+x
            if self.values['name_regex_bool'].get():
                x+="regex, "
            x+=self.values['name_mod'].get()
            x+="): "

            x+=str(self.listify(self.name_entry.get(1.0,END)))
            x='\n        '+x

            output += x

        #comment karma
        if self.values['c_karma_bool'].get():
            x='\n        comment_karma: "'
            x+=self.values['c_karma_mod'].get()
            x+=" "
            x+=self.values['c_karma'].get()
            x+='"'
            output+=x

        #link karma
        if self.values['l_karma_bool'].get():
            x='\n        link_karma: "'
            x+=self.values['l_karma_mod'].get()
            x+=" "
            x+=self.values['l_karma'].get()
            x+='"'
            output+=x

        #combined karma
        if self.values['t_karma_bool'].get():
            x='\n        combined_karma: "'
            x+=self.values['t_karma_mod'].get()
            x+=" "
            x+=self.values['t_karma'].get()
            x+='"'
            output+=x

        #account age
        if self.values['age_bool'].get():
            x='\n        account_age: "'
            x+=self.values['age_mod'].get()
            x+=" "
            x+=self.values['age'].get()
            x+='"'
            output+=x


        #action items

        #approve/remove/spam/filter + reason
        if self.values['moderate_bool'].get():
            x='\n    action: '
            x+=self.values['moderate_action'].get()
            x+='\n    action_reason: '
            x+=self.values['reason_text'].get()
            output+=x

        #leave comment
        if self.values['comment_bool'].get():
            x='\n    comment: |\n'
            x+=self.yamlfy_text(self.comment_entry.get(1.0,END))
            output+=x

        #send modmail
        if self.values['modmail_bool'].get():
            x='\n    modmail: |\n'
            x+=self.yamlfy_text(self.modmail_entry.get(1.0,END))
            output+=x

        #send pm
        if self.values['message_bool'].get():
            x='\n    message: |\n'
            x+=self.yamlfy_text(self.message_entry.get(1.0,END))
            output+=x


        #print(output)
        return output
        
if __name__=="__main__":
    a=Application()
