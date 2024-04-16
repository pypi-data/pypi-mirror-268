from .models import TaskTypes

TRANSLATE_PROMPT_TEMPLATE = """Detect the language of the following transcript. In addition, translate the transcript from the detected language to English.

Transcript:
```
**Skript 01 - Anfrage zu Gebühren und Zinsen auf Kontoauszügen**

**Call-Center-Mitarbeiter (CCM):** "Grüezi, hie isch de [Mitarbeitername] vo de [Bankname] Chundebetreuig. Wie cha ich Ihne hütt hälfe?"

**Chunde (K):** "Hallo, ich bi de [Chundenäme]. Ich ha mine Kontoauszug überprüeft und ha e paar Froge zu de Gebühre und Zinse, wo druf ufgfüehrt sind."

**CCM:** "klar, da cha ich Ihne sicher witerhelfe. Chönd Sie mir bitte Ihri Kontonummer und ihres geburtsdatum gä, damit ich sie verifiziere und Ihres Konto überprüefe cha?"

**K:** "Natürlich, mini Kontonummer isch [Nummer] und bis geburtsdatum isch [Datum]. Es gaht speziell um e paar Gebühre, wo ich nöd ganz verstah."

**CCM:** "Okay, ich lueg mir das a. Einen Moment bitte... So, ich ha Ihres Konto jetz offe. Chönd Sie mir säge, um weli Gebühre es sich handlet?"

**K:** "Da isch e Gebühr druf mit em Titel 'Kontoführigsgebühr' und no eini, wo 'Überzugszins' heisst. Ich ha dänkt, dass ich kei Gebühre ha, und ich verstah nöd, was de Überzugszins isch."

**CCM:** "Ich cha das erkläre. D'Kontoführigsgebühr isch e standardisierti Gebühr, wo mir für d'Führung Ihres Kontos verlange. Die Höchi vo dä Gebühr cha abhängig vo Ihrem Kontomodell si. Zum Überzugszins: Das isch e Zins, wo mir verrechne, wenn Sie mehr Geld usgä, als uf Ihrem Konto verfüegbar isch, also wenn Sie Ihres Konto überzieh."

**K:** "Ah, das macht Sinn. Aber ich bi mir eigentlich sicher, dass ich nie meh usgä ha, als uf mim Konto gsi isch."

**CCM:** "Ich cha das gern no einisch überprüefe. Ei Moment bitte... Ja, ich gseh, dass es e kurze Moment gä hed, wo Ihres Konto leicht überzoge gsi isch. Das chönnt d'Erklärig für dr Überzugszins si."

**K:** "Okay, das muess ich demfall überseh ha. Und chann ich ebbis mache, um die Gebühre z'vermeide?"

**CCM:** "Für d'Kontoführigsgebühr, wenn Sie e Kontomodell mit niedrigere oder gar kei Gebühre wönd, chönnted mir über e Kontowächsel reden. Für de Überzugszins empfehl ich Ihne, regelmässig Ihres Konto z'überprüefe und sicherzustelle, dass genug Geld verfüegbar isch, bevor Sie grösseri Usgabe tätiged."

**K:** "Das tönt vernünftig. Ich wärde über en Kontowächsel nochdänke. Chönd Sie mir Informatione zu de verschiedene Kontomodell schicke?"

**CCM:** "Sicher, ich cha Ihne e Übersicht per E-Mail schicke. Isch Ihri E-Mail-Adrässe bi eus aktuell?"

**K:** "Jo, das isch sie. Vielen Dank für Ihri Hilf und Erklärige."

**CCM:** "Es freut mi, dass ich Ihne cha hälfe. Schicke Ihne gliich die Informatione. Falls no öppis isch, mir sind gern für sie da. E schöne Tag no, [Chundenäme]!"

**K:** "Danke, Ihne au. Uf Wiederhöre."

**CCM:** "Uf Wiederhöre!"
```

Output:
```
Language:
Swiss German

Translation:
**Script 01 - Inquiry About Fees and Interest on Account Statements**

**Call-Center Employee (CCE):** "Hello, this is [Employee Name] from [Bank Name] Customer Service. How can I help you today?"

**Customer (C):** "Hello, I'm [Customer Name]. I've reviewed my account statement and I have some questions about the fees and interest that are listed."

**CCE:** "Sure, I can certainly help you with that. Could you please give me your account number and your date of birth so I can verify your identity and check your account?"

**C:** "Of course, my account number is [Number] and my birthdate is [Date]. It’s specifically about a few fees that I don’t quite understand."

**CCE:** "Okay, let me take a look at that. One moment please... Alright, I have your account open now. Can you tell me which fees you are referring to?"

**C:** "There is a fee listed with the title 'Account Management Fee' and another one called 'Overdraft Interest.' I thought that I didn’t have any fees, and I don’t understand what the overdraft interest is."

**CCE:** "I can explain that. The account management fee is a standardized fee that we charge for the administration of your account. The amount of this fee can vary depending on your account model. As for the overdraft interest: this is an interest we charge if you spend more money than is available in your account, so if you overdraw your account."

**C:** "Ah, that makes sense. But I am actually quite sure that I never spent more than what was in my account."

**CCE:** "I can check that again for you. One moment please... Yes, I see there was a brief moment when your account was slightly overdrawn. That could explain the overdraft interest."

**C:** "Okay, I must have overlooked that. And can I do something to avoid these fees?"

**CCE:** "For the account management fee, if you want an account model with lower or no fees, we could talk about switching accounts. For the overdraft interest, I recommend you regularly check your account and make sure there is enough money available before making larger expenses."

**C:** "That sounds reasonable. I will think about switching accounts. Can you send me information about the different account models?"

**CCE:** "Certainly, I can send you an overview by email. Is your email address up to date with us?"

**C:** "Yes, it is. Thank you for your help and explanations."

**CCE:** "I'm glad I could help. I will send you the information right away. If there is anything else, we are here for you. Have a nice day, [Customer Name]!"

**C:** "Thank you, you too. Goodbye."

**CCE:** "Goodbye!"
```

Transcript:
```
{content}
```

Output:
"""


ANNOTATE_PROMPT_TEMPLATE = """Summarize the following transcript in one sentence. In addition, given the transcript, extract the customer's requests, questions or problems as well as the call-center employee's corresponding response. Extraction should be detailed and cite the related content in the transcript. Citation should be enclosed within the round brakets following the extration. Extraction from the customer's messages should be classified into one of three classes: Request, Question, Problem. 

Definitions of three classes Request, Question, Problem:
```
Class name: Request
Description: The customer is requesting something. They might say they are needing information about something to be sent to their email address or mail address.

Class name: Question
Description: The customer is asking a technical question or a how-to question about the products or services.

Class name: Problem
Description: The customer is describing a problem they are having. They might say they are trying something, but it's not working. They might say they are getting an error or unexpected results.
```

Transcipt:
```
**Script 01 - Inquiry About Fees and Interest on Account Statements**

**Call-Center Employee (CCE):** "Hello, this is [Employee Name] from [Bank Name] Customer Service. How can I help you today?"

**Customer (C):** "Hello, I'm [Customer Name]. I've reviewed my account statement and I have some questions about the fees and interest that are listed."

**CCE:** "Sure, I can certainly help you with that. Could you please give me your account number and your date of birth so I can verify your identity and check your account?"

**C:** "Of course, my account number is [Number] and my birthdate is [Date]. It’s specifically about a few fees that I don’t quite understand."

**CCE:** "Okay, let me take a look at that. One moment please... Alright, I have your account open now. Can you tell me which fees you are referring to?"

**C:** "There is a fee listed with the title 'Account Management Fee' and another one called 'Overdraft Interest.' I thought that I didn’t have any fees, and I don’t understand what the overdraft interest is."

**CCE:** "I can explain that. The account management fee is a standardized fee that we charge for the administration of your account. The amount of this fee can vary depending on your account model. As for the overdraft interest: this is an interest we charge if you spend more money than is available in your account, so if you overdraw your account."

**C:** "Ah, that makes sense. But I am actually quite sure that I never spent more than what was in my account."

**CCE:** "I can check that again for you. One moment please... Yes, I see there was a brief moment when your account was slightly overdrawn. That could explain the overdraft interest."

**C:** "Okay, I must have overlooked that. And can I do something to avoid these fees?"

**CCE:** "For the account management fee, if you want an account model with lower or no fees, we could talk about switching accounts. For the overdraft interest, I recommend you regularly check your account and make sure there is enough money available before making larger expenses."

**C:** "That sounds reasonable. I will think about switching accounts. Can you send me information about the different account models?"

**CCE:** "Certainly, I can send you an overview by email. Is your email address up to date with us?"

**C:** "Yes, it is. Thank you for your help and explanations."

**CCE:** "I'm glad I could help. I will send you the information right away. If there is anything else, we are here for you. Have a nice day, [Customer Name]!"

**C:** "Thank you, you too. Goodbye."

**CCE:** "Goodbye!"
```

Output:
```
Summary:
The customer called to inquire about unexpected fees and interest charges on their bank account statement, and the call-center employee explained the charges and discussed potential ways to avoid them in the future.

Customer's requests, questions or problems:
Customer's Question: 
The customer questioned the 'Account Management Fee' and 'Overdraft Interest' listed on their account statement, expressing confusion over their existence since they believed their account should not have any fees and they had not overspent their account balance ("There is a fee listed with the title 'Account Management Fee' and another one called 'Overdraft Interest.' I thought that I didn’t have any fees, and I don’t understand what the overdraft interest is.").
Call-Center Employee's Response:
The call-center employee clarified that the 'Account Management Fee' is a standard fee for account administration, dependent on the account model, and 'Overdraft Interest' is charged when the account balance goes negative, even briefly ("The account management fee is a standardized fee that we charge for the administration of your account. The amount of this fee can vary depending on your account model. As for the overdraft interest: this is an interest we charge if you spend more money than is available in your account, so if you overdraw your account.").

Customer's Problem: 
The customer was certain they never exceeded their account balance and needed clarification on the recorded overdraft ("Ah, that makes sense. But I am actually quite sure that I never spent more than what was in my account.").
Call-Center Employee's Response:
Upon further review, the employee confirmed that the customer's account was indeed briefly overdrawn, which led to the overdraft charge ("I can check that again for you. One moment please... Yes, I see there was a brief moment when your account was slightly overdrawn. That could explain the overdraft interest.").

Customer's Question: 
The customer asked for ways to avoid these fees in the future ("Okay, I must have overlooked that. And can I do something to avoid these fees?").
Call-Center Employee's Response:
The employee suggested regularly monitoring the account to avoid overdrafts and discussed the possibility of switching to a different account model to reduce or eliminate the management fee ("For the account management fee, if you want an account model with lower or no fees, we could talk about switching accounts. For the overdraft interest, I recommend you regularly check your account and make sure there is enough money available before making larger expenses.").

Customer's Request:
The customer requested information about different account models that might not carry the same fees ("That sounds reasonable. I will think about switching accounts. Can you send me information about the different account models?").
Call-Center Employee's Response:
The employee agreed to send information on different account models via email and confirmed that they had the correct email address on file ("Certainly, I can send you an overview by email. Is your email address up to date with us?").
```

Transcipt:
```
{content}
```

Output:"""


CHAT_PROMPT_TEMPLATE = """You are a virtual assistant. Given the following transcript and the current conversation between a user and the assistant, answer any user query by using information from the transcript. The response should be detailed and cite the related content in the transcript.

Transcript:
```
**Script 01 - Inquiry About Fees and Interest on Account Statements**

**Call-Center Employee (CCE):** "Hello, this is [Employee Name] from [Bank Name] Customer Service. How can I help you today?"

**Customer (C):** "Hello, I'm [Customer Name]. I've reviewed my account statement and I have some questions about the fees and interest that are listed."

**CCE:** "Sure, I can certainly help you with that. Could you please give me your account number and your date of birth so I can verify your identity and check your account?"

**C:** "Of course, my account number is [Number] and my birthdate is [Date]. It’s specifically about a few fees that I don’t quite understand."

**CCE:** "Okay, let me take a look at that. One moment please... Alright, I have your account open now. Can you tell me which fees you are referring to?"

**C:** "There is a fee listed with the title 'Account Management Fee' and another one called 'Overdraft Interest.' I thought that I didn’t have any fees, and I don’t understand what the overdraft interest is."

**CCE:** "I can explain that. The account management fee is a standardized fee that we charge for the administration of your account. The amount of this fee can vary depending on your account model. As for the overdraft interest: this is an interest we charge if you spend more money than is available in your account, so if you overdraw your account."

**C:** "Ah, that makes sense. But I am actually quite sure that I never spent more than what was in my account."

**CCE:** "I can check that again for you. One moment please... Yes, I see there was a brief moment when your account was slightly overdrawn. That could explain the overdraft interest."

**C:** "Okay, I must have overlooked that. And can I do something to avoid these fees?"

**CCE:** "For the account management fee, if you want an account model with lower or no fees, we could talk about switching accounts. For the overdraft interest, I recommend you regularly check your account and make sure there is enough money available before making larger expenses."

**C:** "That sounds reasonable. I will think about switching accounts. Can you send me information about the different account models?"

**CCE:** "Certainly, I can send you an overview by email. Is your email address up to date with us?"

**C:** "Yes, it is. Thank you for your help and explanations."

**CCE:** "I'm glad I could help. I will send you the information right away. If there is anything else, we are here for you. Have a nice day, [Customer Name]!"

**C:** "Thank you, you too. Goodbye."

**CCE:** "Goodbye!"
```

Dialogue: 
```
Assistant: How could I help you?
User: How to avoid account management fees?
Assistant: To avoid account management fees, you may consider switching to a different account model that may have lower or no fees associated with it ("For the account management fee, if you want an account model with lower or no fees, we could talk about switching accounts").
User: What is the overdraft interest?
Assistant: The overdraft interest is an interest charge applied when you spend more money than is available in your account, essentially when your account balance goes negative ("As for the overdraft interest: this is an interest we charge if you spend more money than is available in your account, so if you overdraw your account").
```

Transcript:
```
{content}
```

Answer:
"""


def get_prompt(task: str | TaskTypes, **kwargs) -> str:
    if task == TaskTypes.TRANSLATION.value or task == TaskTypes.TRANSLATION:
        return TRANSLATE_PROMPT_TEMPLATE.format(**kwargs)
    if task == TaskTypes.ANNOTATION.value or task == TaskTypes.ANNOTATION:
        return ANNOTATE_PROMPT_TEMPLATE.format(**kwargs)
    if task == TaskTypes.CHAT.value or task == TaskTypes.CHAT:
        return CHAT_PROMPT_TEMPLATE.format(**kwargs)
    raise ValueError(f'Unsupported task: "{task}"')
