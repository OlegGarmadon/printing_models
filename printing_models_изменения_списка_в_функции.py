#список моделей которые необходимо напечатать.
unprinted_designs = ['phone case', 'robot', 'rd12 robot']
compeleted_models = []

"""
 Цикл последовательно печатает каждую модель до конца списка
 После печати каждая модель перемещаеться в список completed_models.
"""
while unprinted_designs:# Цикл while эмитирует печать каждой модели с конца.
	current_disign = unprinted_designs.pop()# Сохраняеться в данном списке после печати.
	print(f"presiting model: {current_disign}")
	compeleted_models.append(current_disign)

#Вывод всех готовых моделcей.
print("\nThe following models have benn printed:") #Следующие модели были напечатаны
for compeleted_model in compeleted_models:# затем модель перемещаеться в список напечатанных.
	print(compeleted_model) 


# БОЛЕЕ ЭФИКТИВНАЯ ПРОГРАММА.

def print_models(unprinted_design, compeleted_models):
	"""
	Эмитируеться печать моделей, пока список не станет пуустым.
	Каждая модель после печати перемещаеться в пустой список completed_models
	"""
	while unprinted_designs:
		corrent_desing = unprinted_designs.pop()
		print(f"presiting model: {current_disign}")
		compeleted_models.append(current_disign)

def show_completed_models(compeleted_model):
	"""Выводит информацию обо всех напечатанных моделях."""
	print("\nThe following models have benn printed:")
	for compeleted_model in compeleted_models:
		print(compeleted_model)

unprinted_designs = ['phone case', 'robot', 'rd12 robot']
compeleted_models = []

print_models(unprinted_designs, compeleted_models)# [:] передан не сам список а копия если необходимо защетить оригинал. 
show_completed_models(compeleted_models)


