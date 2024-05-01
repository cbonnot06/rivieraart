from django.db import models

# Create your models here.
class Personne(models.Model):
    Civilite = models.CharField(max_length=100)
    EstArtiste = models.CharField(max_length=100)
    EstClient = models.CharField(max_length=100)
    Nom = models.CharField(max_length=100)
    Prenom = models.CharField(max_length=100)
    NomArtiste = models.CharField(max_length=100)
    Adresse = models.CharField(max_length=100)
    AdresseFacturation = models.CharField(max_length=100)
    MotDePasse = models.CharField(max_length=100)
    Abonnement = models.CharField(max_length=100)
    EstAbonneListe1 = models.CharField(max_length=100)
    EstAbonneListe2 = models.CharField(max_length=100)
    EstAbonneListe3 = models.CharField(max_length=100)
    DateCreation = models.CharField(max_length=100)
    DateModification = models.CharField(max_length=100)

class LigneAdresse(models.Model):
    LigneAdresse1 = models.CharField(max_length=100)
    LigneAdresse2 = models.CharField(max_length=100)
    LigneAdresse3 = models.CharField(max_length=100)
    CodePostal = models.CharField(max_length=100)
    Ville = models.CharField(max_length=100)
    Pays = models.CharField(max_length=100)
    TelPro = models.CharField(max_length=100)
    TelPerso = models.CharField(max_length=100)
    MailPerso = models.CharField(max_length=100)
    MailPro = models.CharField(max_length=100)
    DebutValidite = models.CharField(max_length=100)
    FinValidite = models.CharField(max_length=100)
    DateCreation = models.CharField(max_length=100)
    DateModification = models.CharField(max_length=100)


class Oeuvre(models.Model):
    IdArtiste = models.CharField(max_length=100)
    Nom = models.CharField(max_length=100)
    Description = models.CharField(max_length=100)
    Categorie = models.CharField(max_length=100)
    TypeOeuvre = models.CharField(max_length=100)
    PrixAchat = models.CharField(max_length=100)
    PrixLocation = models.CharField(max_length=100)
    Frais1 = models.CharField(max_length=100)
    Frais2 = models.CharField(max_length=100)
    Frais3 = models.CharField(max_length=100)
    DateCreation = models.CharField(max_length=100)
    DateModification = models.CharField(max_length=100)


class ResourcePhoto(models.Model):
    IdResource = models.CharField(max_length=100)
    TypeResource = models.CharField(max_length=100)
    Url = models.CharField(max_length=100)
    Metadata = models.CharField(max_length=100)
    DateCreation = models.CharField(max_length=100)
    DateModification = models.CharField(max_length=100)


class Abonnement(models.Model):
    Nom = models.CharField(max_length=100)
    Description = models.CharField(max_length=100)
    Montant = models.CharField(max_length=100)
