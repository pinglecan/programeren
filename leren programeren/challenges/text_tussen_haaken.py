def unscrambler(zin):
    stukjes = ''

    unscrambled = ''


    for blokhaaken in zin:

        if blokhaaken == '[':

            stukjes = ''
        elif blokhaaken == ']':

            unscrambled += stukjes + ' '
            stukjes = ''
        else:

            stukjes += blokhaaken
    return unscrambled



tekst = "En ze stu[re]n [i]ngekleurde prentbriefkaarten van plekken waarvan ze zich niet reali[s]eren dat ze er nooit zijn geweest zijn [a]an 'Iedereen op nummer 22, weer is prachti[g], onz[e] kamer is aa[n]gekruisd. Missen jullie. E[t]en[]i[s] vettig, maar we hebben een geweldig leuk restaurantje gevonden in de achterstraatjes waar ze Heine[ke]n hebben en kaas en uiten chips en iemand die Een beejte verliefd speel[t] op een a[c]cordeon ' en je zit vier dagen vast op Schip[h]ol voor je vijfdaagse vliegvakantie met niks anders te eten dan uitgedroogde voorverpakte boterhammen..."

print(unscrambler(tekst))