# Description d'algorithme - Langage EXALGO

La définition précise (due à J.G. Penaud) permet de fixer les quelques règles élémentaires permettant d'écrire des algorithmes en s'affranchissant l'implémentation.

## Généralités

Le langage EXALGO est composé de chaînes de caractères alphanumériques, de signes opératoires, de mot-clés réservés, et de signes de ponctuation : **équote;,=, ;,(,), début, fin, //**.
Les marqueurs de fin, début et fin peuvent être remplacés par **{** et **}** lorsqu'il y a encombrement.

## Type

Types prédéfinis : **entier, car, booléen, réél**

Définition de type :
```
type NomDeType= TypePrédéfini;
```

Définition d'un tableau d'entiers :
```
type NomDeType = tableau 1..limite de TypePrédéfini;
```

## Variables

```
var NomDeVariable: TypePrédéfini;
```

## Expressions

Consituées à l'aide de variables déjà déclarées, de parenthèses et d'opérateurs du (des) type(s) des variables concernées.

## Instructions simples

### Affectation

```
NomDeVariable = ExressionDuTypeDeLavariable;
```

### Sortie de calcul

**exit, retourne()** 

## Structure de contrôle

### Bloc d'instruction

```
instruction1
instruction2
.............
```

### Alternative

```
si ExpressionBooléenne alors
    BlocInstruction1
sinon
    BlocInstruction2
finsi;
```
### Alternative multiple

```
selon que
    cas  cas1 : BlocInstruction1
    cas  cas2 : BlocInstruction2
    .............
    autrement :  BlocInstruction
finselonque
```

### Répétition

**exit** permet d'arrêter la répétition

- le bloc d'instruction peut ne pas être éxécuté 

```
tant queExpressionBooléenne faire 
    BlocInstruction
fintantque;
```

- le bloc d'instruction peut ne pas être exécuté et il y a une variable indicatrice

```
pour VariableIndicatrice  
    allant de  ValeurInitiale à ValeurFinale 
    par pas de ValeurPas faire
        BlocInstruction
finpour;
```

- le bloc d'instruction est exécuté au moins une fois

```
répéter
    BlocInstruction
jusqu'à ExpressionBooléenne finrépéter;
```

## Fonctions

Une fonction retourne une valeur par l'instruction simple(**retourne**(Expression)).
Une fonction s'utilise dans le calcul d'une expression ou comme instruction simple.

### Ecriture de la fonction

```
fonction NomDeFonction (ListeParamètres):Typerésultat;
    //déclarations des variables locales autres que les paramètres 
    début
    // partie instruction qui contient l'appel à retourne()
    fin
finFonction
```

### Liste des paramètres
Les paramètres sont passés
- par référence ref, on écrit
```
val ListeVariable:NomDeType
```
- par valeur val, on écrit
```
ref ListeVariable:NomDeType
```

Le type du résultat est vide si la fonction ne renvoie pas de résultat. 


## Types

### Type structuré
Un type structuré est constitué à partir de types de base ou d'autres types déclarés.

```
type NomDeType: structure
    champ1:NomDeType1
    champ2:NomDeType2
        ...........................
finstructure
```

Après la déclaration
```
var E:NomDeTypeEnregistrement
```

on accède au différents champs par le nom de la variable suivi d'un **point** suivi du nom de champ (E.champ1)

### Type pointeur
Si O est un objet de type T, on accède à l'objet par O^. Si on déclare :

```
var P:^NomDeType
```

alors on peut obtenir un objet accessible par allouer(P).
Lorsqu'on n'utilise plus l'objet, il faut libérer l'espace qu'il utilise par desallouer(P). 