import json
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
from .openfunctions_utils import strip_function_calls, parse_function_call
import pandas as pd
from googletrans import Translator
from tqdm import tqdm
import re





class ALSA:
    def __init__(self,model_path): 

        self.device : str = "cuda:0" if torch.cuda.is_available() else "cpu"
        self.torch_dtype = torch.float16 if torch.cuda.is_available() else torch.float32
        self.model_id = model_path#"/run/user/1001/gvfs/smb-share:server=192.168.10.5,share=devel/S.Eghdami/gorilla"
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_id)
        self.model = AutoModelForCausalLM.from_pretrained(self.model_id, torch_dtype=self.torch_dtype, low_cpu_mem_usage=True).to(self.device)
        self.pipe = pipeline(
        "text-generation",
        model=self.model,
        tokenizer=self.tokenizer,
        max_new_tokens=64,
        batch_size=16,
        torch_dtype=self.torch_dtype,
        device=self.device,)
    def __getprompt__(self,comment,product):

        
        aspect_rate_prompt_template=f"""
        i give a user comment about the product "{product}". 
        
        Comment: Hello. This phone has a beautiful design and color. The user environment is very intuitive. Charging and battery performance and charging speed are excellent. The camera is also acceptable. I recommend buying it, especially the white color, which is extremely beautiful.
        Aspect: design (5), color (5), user interface (5), charging (5), camera (3)
        
        Comment: Sir, he has no problem with this price. Buy it and enjoy it
        Aspect: Price (5), Overall (5)
        
        Comment: It is used a lot and can be done, but the quality of the bag is low. Overall, it is good
        Aspect: efficiency (5), bag (1), overall (4)
        
        Comment: It is necessary in every home
        Aspect: efficiency (4)
        
        Comment: In general, it is a good phone for normal work, but sometimes (1) the antenna jumps or the internet is interrupted, which must be turned off and on. (2) In the heat of summer, if the phone gets hot, the screen will not show anything and you have to wait for the mobile phone to cool down. (3) 128GB memory and 6GB RAM is good, but it doesn't have a good chipset, cpu, and graphics card, and it only handles normal games. (4) It was Android 11 on the first day, but now it has been upgraded to Android 13. (5) It has a good camera and battery.
        Aspect: antenna (2), hardware (2), camera (3), battery (3)
        
        Comment: The sound quality of these headphones is amazing, providing clear and crisp audio. However, the build quality feels a bit flimsy, and the ear cushions are not very comfortable for long listening sessions.
        Aspect: sound quality (5), build quality (2), comfort (2)

        Comment: This restaurant serves delicious food with generous portion sizes. However, the service can be slow during peak hours, and the ambiance is lacking compared to other eateries in the area.
        Aspect: food quality (5), service (2), ambiance (3)

        Comment: The customer service provided by this company is exceptional, with representatives being courteous and helpful at all times. However, the delivery times for their products can be quite long, causing inconvenience to customers.
        Aspect: customer service (5), delivery speed (2)

        Comment: The user interface of this software is intuitive and user-friendly, making it easy to navigate and use. However, the lack of certain features limits its functionality for more advanced users.
        Aspect: user interface (5), functionality (3)

        Comment: The performance of this laptop is outstanding, handling demanding tasks with ease. However, the battery life is disappointingly short, requiring frequent recharges throughout the day.
        Aspect: performance (5), battery life (2)
        
        
        Rating Assignment: Assign a numerical rating between 0 and 5 to each aspect based on the evaluated sentiment. The rating should reflect the degree of satisfaction or quality as perceived by the user. Use the following scale as a guide:

        0: Very Poor - The user expresses strong dissatisfaction or indicates severe issues with the aspect.
        1: Poor - The user indicates dissatisfaction or minor issues with the aspect.
        2: Fair - The comment suggests mixed feelings or a neutral stance towards the aspect.
        3: Good - The user shows satisfaction with the aspect but may mention minor drawbacks.
        4: Very Good - The comment is positive, with the user expressing satisfaction and only negligible criticisms, if any.
        5: Excellent - The user expresses high satisfaction, praising the aspect with no reservations.
            
        try to extract dominant aspects mentioned in the comment like done in the example above, you must add overall aspect:
        
        comment: {comment}
        Aspect:"""
    
    
        return aspect_rate_prompt_template


    def get_english_translation(self,text):

        translator=Translator()

        translated_text=translator.translate(text,dest='en').text

        return translated_text
    
    def get_persian_translation(self,text):

        translator=Translator()

        translated_text=translator.translate(text,dest='fa').text

        return translated_text
    
    def get_aspect_rates(self,prompt):
        output = self.pipe(prompt)

        return output[0]['generated_text'].split(prompt)[1].split('\n')[0]
    
    # def analyse_single_comment(self,comment,product):

    #     translated_comment=self.get_english_translation(comment)
    #     translated_product=self.get_english_translation(product)
    #     prompt = self.__getprompt__(translated_comment,translated_product)
    #     aspect_rate =self.get_aspect_rates(prompt)
    #     return aspect_rate

    def feature_counting(self,topics):
        c = dict()
        overall = [0,0]
        for i in tqdm(range(len(topics))):
            # print(data.iloc[i].text)
            if len(topics[i])!=0:
                ts = topics[i].split(",")
                for t in ts:
                    res = re.split(r"[\(\)]", t)
                    if res[0].strip() != "" and res[0].strip().lower() != 'none' and len(res)>1:
                        key = (self.get_persian_translation(re.sub("\.","",res[0]).strip()), re.sub("\.","",res[0]).strip().lower())
                        if re.sub("\.","",res[0]).strip().lower() == 'overall':
                            if int(res[1]) >= 3:
                                overall[0] += 1
                            if int(res[1]) <=2:
                                overall[1] += 1
                        else:
                            if key in c.keys():
                                try:
                                    c[key].append(int(res[1]))

                                except:
                                    pass
                            else:
                                try:
                                    c[key] = [int(res[1])]
                                except:
                                    pass
        return c , overall

    def get_json_report(self,c,overall,product):

        sorted_c = sorted(list(c.items()), key=lambda x:-len(x[1]))
        total=[]
        for s in sorted_c:
            aspects=s[0][0]+' '+s[0][1]
            positive_count,negative_count=0,0
            for rating in s[1]:
                if int(rating)<=2:
                    negative_count+=1
                if int(rating)>=3:
                    positive_count+=1
            total.append({"aspect":aspects,"negative_comments":negative_count,"positive_comments":positive_count})

        

        sorted_neg = sorted(c.items(), key=lambda x: sum(1 for v in x[1] if v< 3),reverse=True)
        most_negative_list=[]
        for sn in sorted_neg:
            aspects=sn[0][0]+' '+sn[0][1]
            negative_count=0
            for rating in sn[1]:
                if int(rating)<=2:
                    negative_count+=1
            most_negative_list.append({"aspect":aspects,"negative_comments":negative_count})


        sorted_pos=sorted(c.items(), key=lambda x: sum(1 for v in x[1] if v>= 3),reverse=True)
        most_positive_list=[]
        for sp in sorted_pos:
            aspects=sp[0][0]+' '+sp[0][1]
            positive_count=0
            for rating in sp[1]:
                if int(rating)>=3:
                    positive_count+=1
            most_positive_list.append({"aspect":aspects,"positive_comments":positive_count})


        data_dict={"overall":[{"suggested":overall[0],"not_suggested":overall[1]}],"product_name":product,"total":total,"most_negative":most_negative_list,"most_positive":most_positive_list}
        return data_dict




    def analyse_comments(self,data,product):

        comments_df=pd.DataFrame({"fa": data})
        comments_df['en']=comments_df['fa'].apply(self.get_english_translation)
        comments_df['aspect_rate']=comments_df['en'].apply(lambda x: self.get_aspect_rates(self.__getprompt__(x,product)))

        aspect_rate_list=comments_df['aspect_rate'].tolist()
        c,overall=self.feature_counting(aspect_rate_list)

        result=self.get_json_report(c,overall,product)

        


        return result
        


    

