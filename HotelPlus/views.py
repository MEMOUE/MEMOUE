import time

from django.shortcuts import render
import io
from datetime import datetime
from django.http import FileResponse, HttpResponse
from django.views import View
from reportlab.pdfgen import canvas


# from reportlab.lib.pagesizes import letter


def index(request):
    return render(request, "index.html")


class Facture(View):
    def post(self, request):
        if request.method == "POST":
            temps = datetime.now()
            nom = request.POST.get("nom")
            prenom = request.POST.get("prenom")
            service = request.POST.get("service")
            montant = request.POST.get("montant")
            #logo = request.FILES.get("logo")

            logo = "C:/Users/mamad/Documents/L3_GLSI/logotype.png"

            buffer = io.BytesIO()
            c = canvas.Canvas(buffer, pagesize=(300, 400))

            c.drawString(10, 380, "Nom : {}".format(nom))
            c.drawString(10, 330, "Prenom : {}".format(prenom))
            c.drawString(10, 280, "Service : {}".format(service))
            c.drawString(10, 230, "Montant : {}".format(montant))
            c.drawString(100, 230, "FCFA")
            c.drawImage(logo, 100, 70, width=100, height=100)
            c.drawString(75, 10, f"Fait le : "
                                 f"{temps.day}-{temps.month}-{temps.year} à {temps.hour}h:{temps.minute}min:{temps.second}s"
                         )

            c.showPage()
            c.save()

            buffer.seek(0)
            return FileResponse(buffer, as_attachment=True, filename="test.pdf")

    def get(self, request):
        return render(request, "facture.html")


def pdf(request):
    """
    buffer = io.BytesIO()
    p = canvas.Canvas(buffer)
    p.drawString(0, 820, "Bonjour je suis MTB qui signifie litteralement Mamadou Tahirou BAH et c'est égalment mon nom propre"
                       "c'est à dire le nom que mes parents m'ont donné donc voilà c'est tout moi")
    p.showPage()
    p.save()

    buffer.seek(0)

    return FileResponse(buffer, as_attachment=True, filename="mtb.pdf")
    """
    # Créez une réponse HTTP avec le type de contenu PDF
    response = HttpResponse(content_type='application/pdf')

    # Définir le nom du fichier PDF
    response['Content-Disposition'] = 'attachment; filename="example.pdf"'

    # Créez un objet canvas pour dessiner le contenu du PDF
    p = canvas.Canvas(response)

    # Définir la largeur maximale de la zone de texte
    max_width = 600

    # Définir le texte
    text = "Ceci est un exemple de phrase longue qui nécessite un retour à la ligne si elle dépasse la largeur maximale spécifiée.eci est un exemple de phrase longue qui nécessite un retour à la ligne si elle dépasse la largeur maximale spécifiée."

    # Diviser le texte en lignes
    lines = []
    current_line = ''
    words = text.split(' ')
    for word in words:
        if p.stringWidth(current_line + ' ' + word) <= max_width:
            current_line += ' ' + word
        else:
            lines.append(current_line.strip())
            current_line = word
    lines.append(current_line.strip())

    # Dessiner les lignes de texte
    y = 800
    for line in lines:
        p.drawString(10, y, line)
        y -= 25  # Espacement entre les lignes

    # Enregistrez le contenu du PDF
    p.showPage()
    p.save()

    return response
