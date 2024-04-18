import json
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
# from dalsa.openfunctions_utils import strip_function_calls, parse_function_call
import pandas as pd
from googletrans import Translator
from tqdm import tqdm
import re





class ALSA:
    def __init__(self,model_path): 

        self.device : str = "cuda:0" if torch.cuda.is_available() else "cpu"
        self.torch_dtype = torch.float16 if torch.cuda.is_available() else torch.float32
        self.model_path = model_path#"/run/user/1001/gvfs/smb-share:server=192.168.10.5,share=devel/S.Eghdami/gorilla"
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_path, padding_side='left')
        self.model = AutoModelForCausalLM.from_pretrained(self.model_path, torch_dtype=torch.bfloat16).to(self.device)
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
    
    def get_aspect_rates(self,prompts):
        # output = self.pipe(prompt)

        input_tokens = self.tokenizer(prompts, return_tensors="pt", padding=True).to("cuda")
        output_tokens = self.model.generate(**input_tokens, max_new_tokens=64)
        aspect_rates = [self.tokenizer.batch_decode(output_tokens)[i].split(prompts[i])[1].split('\n')[0] for i in range(len(prompts))]

        return aspect_rates
    
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
            aspects_fa=s[0][0]
            aspect_en=s[0][1]
            positive_count,negative_count=0,0
            for rating in s[1]:
                if int(rating)<=2:
                    negative_count+=1
                if int(rating)>=3:
                    positive_count+=1
            total.append({"aspect_fa":aspects_fa,"aspect_en":aspect_en,"negative_comments":negative_count,"positive_comments":positive_count})

        

        sorted_neg = sorted(c.items(), key=lambda x: sum(1 for v in x[1] if v< 3),reverse=True)
        most_negative_list=[]
        for sn in sorted_neg:
            aspects_fa=sn[0][0]
            aspect_en=sn[0][1]
            negative_count=0
            for rating in sn[1]:
                if int(rating)<=2:
                    negative_count+=1
            most_negative_list.append({"aspect_fa":aspects_fa,"aspect_en":aspect_en,"negative_comments":negative_count})


        sorted_pos=sorted(c.items(), key=lambda x: sum(1 for v in x[1] if v>= 3),reverse=True)
        most_positive_list=[]
        for sp in sorted_pos:
            aspects_fa=sp[0][0]
            aspect_en=sp[0][1]
            positive_count=0
            for rating in sp[1]:
                if int(rating)>=3:
                    positive_count+=1
            most_positive_list.append({"aspect_fa":aspects_fa,"aspect_en":aspect_en,"positive_comments":positive_count})


        data_dict={"overall":[{"suggested":overall[0],"not_suggested":overall[1]}],"product_name":product,"total":total,"most_negative":most_negative_list,"most_positive":most_positive_list}
        return data_dict




    def analyse_comments(self,data,product, batch_size=1):
        comments_df=pd.DataFrame({"fa": data['product_comments']})
        comments_df['en']=comments_df['fa'].apply(self.get_english_translation)
        aspect_rates_list = [None for _ in range(len(comments_df))]
        for i in range(0, len(comments_df), batch_size):
            prompts = [self.__getprompt__(comment,product) for comment in comments_df['en'][i:i+batch_size]]
            aspect_rates_list[i:i+batch_size] = self.get_aspect_rates(prompts)

        # comments_df['aspect_rate']=comments_df['en'].apply(lambda x: self.get_aspect_rates(self.__getprompt__(x,product)))
        # aspect_rate_list=comments_df['aspect_rate'].tolist()

        c,overall=self.feature_counting(aspect_rates_list)

        result=self.get_json_report(c,overall,product)

        


        return result
        


    

