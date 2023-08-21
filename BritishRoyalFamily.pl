parent(queen_elizabeth_ii, prince_charles).
parent(queen_elizabeth_ii, princess_anne).
parent(queen_elizabeth_ii, prince_andrew).
parent(queen_elizabeth_ii, prince_edward).
parent(prince_phillip, prince_charles).
parent(prince_phillip, princess_anne).
parent(prince_phillip, prince_andrew).
parent(prince_phillip, prince_edward).
parent(prince_charles, prince_william).
parent(prince_charles, prince_harry).
parent(princess_diana, prince_william).
parent(princess_diana, prince_harry).
parent(princess_anne, peter_phillips).
parent(princess_anne, zara_phillips).
parent(captain_mark_phillips, peter_phillips).
parent(captain_mark_phillips, zara_phillips).
parent(prince_andrew, princess_beatrice).
parent(prince_andrew, princess_eugenie).
parent(sarah_ferguson, princess_beatrice).
parent(sarah_ferguson, princess_eugenie).
parent(prince_edward, james_viscount_severn).
parent(prince_edward, lady_louise_mountbatten_windsor).
parent(sophie_rhys_jones, james_viscount_severn).
parent(sophie_rhys_jones, lady_louise_mountbatten_windsor).
parent(prince_william, prince_george).
parent(prince_william, princess_charlotte).
parent(kate_middleton, prince_george).
parent(kate_middleton, princess_charlotte).
parent(peter_phillips, savannah_phillips).
parent(peter_phillips, isla_phillips).
parent(autumn_kelly, savannah_phillips).
parent(autumn_kelly, isla_phillips).
parent(zara_phillips, mia_grace_tindall).
parent(mike_tindall, mia_grace_tindall).
male(prince_phillip).
male(prince_charles).
male(captain_mark_phillips).
male(timothy_laurence).
male(prince_andrew).
male(prince_edward).
male(prince_william).
male(prince_harry).
male(peter_phillips).
male(mike_tindall).
male(james_viscount_severn).
male(prince_george).
female(queen_elizabeth_ii).
female(princess_diana).
female(camilla_parker_bowles).
female(princess_anne).
female(sarah_ferguson).
female(sophie_rhys_jones).
female(kate_middleton).
female(autumn_kelly).
female(zara_phillips).
female(princess_beatrice).
female(princess_eugenie).
female(lady_louise_mountbatten_windsor).
female(princess_charlotte).
female(savannah_phillips).
female(isla_phillips).
female(mia_grace_tindall).
married(queen_elizabeth_ii, prince_phillip).
married(prince_charles, camilla_parker_bowles).
married(princess_anne, timothy_laurence).
married(prince_edward, sophie_rhys_jones).
married(prince_william, kate_middleton).
married(peter_phillips, autumn_kelly).
married(zara_phillips, mike_tindall).
married(prince_phillip, queen_elizabeth_ii).
married(camilla_parker_bowles, prince_charles).
married(timothy_laurence, princess_anne).
married(sophie_rhys_jones, prince_edward).
married(kate_middleton, prince_william).
married(autumn_kelly, peter_phillips).
married(mike_tindall,zara_phillips).
divorced(prince_charles, princess_diana).
divorced(princess_anne, captain_mark_phillips).
divorced(prince_andrew, sarah_ferguson).
divorced(princess_diana, prince_charles).
divorced(captain_mark_phillips, princess_anne).
divorced(sarah_ferguson, prince_andrew).
husband(X, Y):- male(X), married(X, Y).
wife(X, Y):- female(X), married(X, Y).
father(X, Y):- male(X), parent(X, Y).
mother(X, Y):- female(X), parent(X, Y).
child(X, Y):- parent(Y, X).
son(X, Y):- male(X), parent(Y, X).
daughter(X, Y):- female(X), parent(Y, X).
grandparent(X, Y):- parent(X, Z), parent(Z, Y).
grandmother(X, Y):- female(X), grandparent(X, Y).
grandfather(X, Y):- male(X), grandparent(X, Y).
grandchild(X, Y):- grandparent(Y, X).
grandson(X, Y):- male(X), grandchild(X, Y).
granddaughter(X, Y):- female(X), grandchild(X, Y).
sibling(X, Y):- mother(Z, X), mother(Z, Y), X \= Y.
brother(X, Y):- male(X), sibling(X, Y).
sister(X, Y):- female(X), sibling(X, Y).
aunt(X, Y):- female(X), sibling(X, Z), parent(Z, Y).
aunt(X, Y):- female(X), married(X, Z), sibling(Z, T), parent(T, Y).
uncle(X, Y):- male(X), sibling(X, Z), parent(Z, Y).
uncle(X, Y):- male(X), married(X, Z), sibling(Z, T), parent(T, Y).
niece(X, Y):- female(X), aunt(Y, X).
niece(X, Y):- female(X), uncle(Y, X).
nephew(X, Y):- male(X), aunt(Y, X).
nephew(X, Y):- male(X), uncle(Y, X).
