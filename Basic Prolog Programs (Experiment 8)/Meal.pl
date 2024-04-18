%Facts
                     
food(burger).	% burger is a food
food(sandwich).	% sandwich is a food
food(pizza).	% pizza is a food
lunch(sandwich).	% sandwich is a lunch
dinner(pizza).	% pizza is a dinner


%Rules	
meal(X) :- food(X).

%Every food is a meal OR
%Anything is a meal if it is a food


/* Queries / Goals	
?- food(pizza).
% Is pizza a food?
?- meal(X), lunch(X).
% Which food is meal and lunch? 
?- dinner(sandwich).
% Is sandwich a dinner?
*/