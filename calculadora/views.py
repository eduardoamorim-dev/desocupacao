from django.shortcuts import render
from calendar import month_name

def index(request):
    context = {
        "resultado": None,
        "mes": "",
        "ano": "",
        "exibir_resultado": False,
        "nome_mes": ""
    }
    
    if request.method == "POST":
        try:
            ceas_mes = int(request.POST.get("mes", 0))
            ceas_ano = int(request.POST.get("ano", 0))
            
            # Validar entrada
            if ceas_mes < 1 or ceas_mes > 12:
                raise ValueError("Mês deve estar entre 1 e 12")
            
            # Nomes dos meses em português
            ceas_nomes_meses = {
                1: "Janeiro",
                2: "Fevereiro",
                3: "Março",
                4: "Abril",
                5: "Maio",
                6: "Junho",
                7: "Julho",
                8: "Agosto",
                9: "Setembro",
                10: "Outubro",
                11: "Novembro",
                12: "Dezembro"
            }
            
            # Obtém o nome do mês em português
            ceas_nome_mes = ceas_nomes_meses[ceas_mes]
            
            # Implementação da fórmula seguindo exatamente o formato solicitado
            ceas_termo1 = 10910413554.0623 * ceas_ano
            ceas_termo2 = 0.982623038037353 * ceas_mes
            ceas_termo3 = -10854680.7406238 * (ceas_ano ** 2)
            ceas_termo4 = -0.497404737430208 * (ceas_mes ** 2)
            ceas_termo5 = 5399.51149416065 * (ceas_ano ** 3)
            ceas_termo6 = 0.0955446990949723 * (ceas_mes ** 3)
            ceas_termo7 = -1.34293043769336 * (ceas_ano ** 4)
            ceas_termo8 = -0.00813519503280296 * (ceas_mes ** 4)
            ceas_termo9 = 0.000133599317804352 * (ceas_ano ** 5)
            ceas_termo10 = 0.000252391410607209 * (ceas_mes ** 5)
            ceas_termo11 = -4386487265240.91
            
            ceas_taxa_estimada = ceas_termo1 + ceas_termo2 + ceas_termo3 + ceas_termo4 + ceas_termo5 + \
                            ceas_termo6 + ceas_termo7 + ceas_termo8 + ceas_termo9 + ceas_termo10 + ceas_termo11
            
            # Formatar o resultado como porcentagem
            context = {
                "resultado": f"{ceas_taxa_estimada:.2f}%",
                "mes": ceas_mes,
                "ano": ceas_ano,
                "nome_mes": ceas_nome_mes,
                "exibir_resultado": True
            }
        except ValueError as e:
            context["erro"] = str(e) if str(e) else "Por favor, insira números válidos para mês e ano"
    
    return render(request, "calculadora/index.html", context)