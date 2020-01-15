import torch
roberta = torch.hub.load('pytorch/fairseq', 'roberta.large')
roberta.eval()

roberta.fill_mask('What do you <mask> from me', topk=3)
# [('The first Star wars movie came out in 1977', 0.9504708051681519, ' 1977'), ('The first Star wars movie came out in 1978', 0.009986862540245056, ' 1978'), ('The first Star wars movie came out in 1979', 0.009574787691235542, ' 1979')]
roberta.fill_mask('RoBERTa can be used to disambiguate <mask>', topk=3)

roberta.fill_mask('I\'m very <mask> to know more about this position', topk=3)

roberta.fill_mask('I will have <mask> access to voicemail or email while I am away.', topk=3)



roberta = torch.hub.load('pytorch/fairseq', 'roberta.large.wsc', user_dir='examples/roberta/wsc')
roberta.eval()
roberta.disambiguate_pronoun('The city councilmen refused the demonstrators a permit because [they] feared violence.')
