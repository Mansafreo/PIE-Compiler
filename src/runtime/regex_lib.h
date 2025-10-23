#ifndef REGEX_LIB_H

#define REGEX_LIB_H

 

#include <stdint.h>

#include <stddef.h>

 

// Maximum number of states in NFA

#define MAX_STATES 256

#define MAX_TRANSITIONS 512

#define EPSILON -1  // Epsilon transition

 

// NFA State

typedef struct {

    int32_t id;

    int32_t is_accept;  // 1 if this is an accept state

} NFAState;

 

// NFA Transition

typedef struct {

    int32_t from_state;

    int32_t to_state;

    int32_t symbol;  // Character or EPSILON

} NFATransition;

 

// NFA Structure

typedef struct {

    NFAState states[MAX_STATES];

    NFATransition transitions[MAX_TRANSITIONS];

    int32_t num_states;

    int32_t num_transitions;

    int32_t start_state;

 

    // Length constraints

    int32_t has_exact_length;

    int32_t exact_length;

    int32_t has_min_length;

    int32_t min_length;

    int32_t has_max_length;

    int32_t max_length;

} NFA;

 

// Regex pattern (compiled NFA)

typedef struct {

    NFA* nfa;

    char* pattern_string;  // Original pattern for debugging

} RegexPattern;

 

// Public API

 

// Create a regex pattern from a string

RegexPattern* regex_compile(const char* pattern);

 

// Match a string against a regex pattern

int32_t regex_match(RegexPattern* regex, const char* str);

 

// Free a regex pattern

void regex_free(RegexPattern* regex);

 

// Internal NFA functions

 

// Create an empty NFA

NFA* nfa_create();

 

// Add a state to the NFA

int32_t nfa_add_state(NFA* nfa, int32_t is_accept);

 

// Add a transition to the NFA

void nfa_add_transition(NFA* nfa, int32_t from, int32_t to, int32_t symbol);

 

// Build NFA from regex pattern

NFA* nfa_from_regex(const char* pattern);

 

// Match string using NFA

int32_t nfa_match(NFA* nfa, const char* str);

 

// Free NFA

void nfa_free(NFA* nfa);

 

// Helper functions for NFA construction

 

// Create NFA for a single character

NFA* nfa_char(char c);

 

// Create NFA for concatenation

NFA* nfa_concat(NFA* nfa1, NFA* nfa2);

 

// Create NFA for alternation (OR)

NFA* nfa_or(NFA* nfa1, NFA* nfa2);

 

// Create NFA for Kleene star

NFA* nfa_star(NFA* nfa);

 

// Create NFA for positive closure

NFA* nfa_plus(NFA* nfa);

 

#endif // REGEX_LIB_H