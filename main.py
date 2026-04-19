import weakref
import gc

class KattaObekt:
    def __init__(self, nom):
        self.nom = nom

    def __del__(self):
        print(f"{self.nom} obekti o'chirildi")

def main():
    katta_obektlar = weakref.WeakValueDictionary()

    for i in range(10):
        obekt = KattaObekt(f"Obekt {i}")
        katta_obektlar[obekt.nom] = obekt

    # Obektlar o'chirilishi uchun GC ni ishga tushuramiz
    gc.collect()

    # Obektlar mavjudligini tekshiramiz
    for nom, obekt in katta_obektlar.items():
        print(f"{nom}: {obekt is None}")

if __name__ == "__main__":
    main()
```

Bunda, biz `weakref.WeakValueDictionary` ni ishlatib, katta obektlar uchun dictionary yaratamiz. `KattaObekt` klassi yaratilganda, u `__del__` metodini o'z ichiga oladi, bu metod obekt o'chirilganda ishlaydi. `main` funksiyasida, biz 10 ta katta obekt yaratib, ularni dictionaryga qo'yamiz. Keyin, biz GC ni ishga tushurib, obektlar mavjudligini tekshiramiz.
