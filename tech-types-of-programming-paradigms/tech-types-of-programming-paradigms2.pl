% Define a rule to check if a number is even
is_even(X) :- 0 is X mod 2.

% Define a rule to check if a number is odd
is_odd(X) :- not(is_even(X)).

% Query to check if a number is even or odd
?- is_even(4).  % Output: true
?- is_odd(7).   % Output: true
