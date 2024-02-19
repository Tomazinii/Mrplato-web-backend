import re
import forms as fms
# Seu código

question = '1 - p → q , ~q ⊢ ~p'

lp = question.split(' - ')  # lp = [index, argument]

input_list = lp[1].replace('|-', fms.GlobalConstants.c_ass)  # Replace '->' by  '⊢'
l_terms = input_list.split(' ' + fms.GlobalConstants.c_ass + ' ')  # Conclusion must appear after ' ⊢ "
# l_terms is a list of 2 elements: a string of premisses and a conclusion
s_premisses = str(l_terms[0])
s_conclusion = l_terms[1]

print("s_premisses",s_premisses)
# Regex para verificar se o padrão está presente em s_premisses
pattern = r'padrão_a_ser_verificado'
if not re.search(pattern, s_premisses):
    raise ValueError("Padrão não encontrado em s_premisses. Regex falhou.")

# Regex para extrair a conclusão de s_conclusion
pattern_conclusion = r'padrão_para_extrair_a_conclusão'
match = re.search(pattern_conclusion, s_conclusion)
if not match:
    raise ValueError("Padrão não encontrado em s_conclusion. Regex falhou.")
conclusion = match.group(0)

# Se o código chegou até aqui, o regex foi bem-sucedido
print("Conclusão extraída com sucesso:", conclusion)
