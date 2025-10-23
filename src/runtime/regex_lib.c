#include "regex_lib.h"

#include <stdlib.h>

#include <string.h>

#include <stdio.h>

#include <ctype.h>

 

// ============================================================================

// NFA Basic Operations

// ============================================================================

 

NFA* nfa_create() {

    NFA* nfa = (NFA*)malloc(sizeof(NFA));

    if (!nfa) return NULL;

 

    nfa->num_states = 0;

    nfa->num_transitions = 0;

    nfa->start_state = 0;

    nfa->has_exact_length = 0;

    nfa->has_min_length = 0;

    nfa->has_max_length = 0;

 

    return nfa;

}

 

int32_t nfa_add_state(NFA* nfa, int32_t is_accept) {

    if (nfa->num_states >= MAX_STATES) return -1;

 

    int32_t state_id = nfa->num_states;

    nfa->states[state_id].id = state_id;

    nfa->states[state_id].is_accept = is_accept;

    nfa->num_states++;

 

    return state_id;

}

 

void nfa_add_transition(NFA* nfa, int32_t from, int32_t to, int32_t symbol) {

    if (nfa->num_transitions >= MAX_TRANSITIONS) return;

 

    nfa->transitions[nfa->num_transitions].from_state = from;

    nfa->transitions[nfa->num_transitions].to_state = to;

    nfa->transitions[nfa->num_transitions].symbol = symbol;

    nfa->num_transitions++;

}

 

void nfa_free(NFA* nfa) {

    if (nfa) free(nfa);

}

 

// ============================================================================

// Thompson's Construction - Basic NFAs

// ============================================================================

 

NFA* nfa_char(char c) {

    NFA* nfa = nfa_create();

    if (!nfa) return NULL;

 

    int32_t start = nfa_add_state(nfa, 0);

    int32_t accept = nfa_add_state(nfa, 1);

 

    nfa->start_state = start;

    nfa_add_transition(nfa, start, accept, (int32_t)c);

 

    return nfa;

}

 

NFA* nfa_concat(NFA* nfa1, NFA* nfa2) {

    if (!nfa1 || !nfa2) return NULL;

 

    NFA* result = nfa_create();

    if (!result) return NULL;

 

    // Copy nfa1 states

    for (int i = 0; i < nfa1->num_states; i++) {

        nfa_add_state(result, nfa1->states[i].is_accept);

    }

 

    // Copy nfa1 transitions

    for (int i = 0; i < nfa1->num_transitions; i++) {

        nfa_add_transition(result, 

            nfa1->transitions[i].from_state,

            nfa1->transitions[i].to_state,

            nfa1->transitions[i].symbol);

    }

 

    // Find accept states of nfa1 and make them non-accept

    for (int i = 0; i < nfa1->num_states; i++) {

        if (nfa1->states[i].is_accept) {

            result->states[i].is_accept = 0;

            // Add epsilon transition to start of nfa2

            nfa_add_transition(result, i, nfa1->num_states, EPSILON);

        }

    }

 

    // Copy nfa2 states (offset by nfa1's state count)

    int offset = nfa1->num_states;

    for (int i = 0; i < nfa2->num_states; i++) {

        nfa_add_state(result, nfa2->states[i].is_accept);

    }

 

    // Copy nfa2 transitions (offset state IDs)

    for (int i = 0; i < nfa2->num_transitions; i++) {

        nfa_add_transition(result,

            nfa2->transitions[i].from_state + offset,

            nfa2->transitions[i].to_state + offset,

            nfa2->transitions[i].symbol);

    }

 

    result->start_state = nfa1->start_state;

 

    nfa_free(nfa1);

    nfa_free(nfa2);

 

    return result;

}

 

NFA* nfa_or(NFA* nfa1, NFA* nfa2) {

    if (!nfa1 || !nfa2) return NULL;

 

    NFA* result = nfa_create();

    if (!result) return NULL;

 

    // New start state

    int32_t new_start = nfa_add_state(result, 0);

    result->start_state = new_start;

 

    // Copy nfa1 states (offset by 1)

    int offset1 = 1;

    for (int i = 0; i < nfa1->num_states; i++) {

        nfa_add_state(result, nfa1->states[i].is_accept);

    }

 

    // Copy nfa1 transitions

    for (int i = 0; i < nfa1->num_transitions; i++) {

        nfa_add_transition(result,

            nfa1->transitions[i].from_state + offset1,

            nfa1->transitions[i].to_state + offset1,

            nfa1->transitions[i].symbol);

    }

 

    // Copy nfa2 states (offset by 1 + nfa1 states)

    int offset2 = 1 + nfa1->num_states;

    for (int i = 0; i < nfa2->num_states; i++) {

        nfa_add_state(result, nfa2->states[i].is_accept);

    }

 

    // Copy nfa2 transitions

    for (int i = 0; i < nfa2->num_transitions; i++) {

        nfa_add_transition(result,

            nfa2->transitions[i].from_state + offset2,

            nfa2->transitions[i].to_state + offset2,

            nfa2->transitions[i].symbol);

    }

 

    // Add epsilon transitions from new start to both NFAs

    nfa_add_transition(result, new_start, nfa1->start_state + offset1, EPSILON);

    nfa_add_transition(result, new_start, nfa2->start_state + offset2, EPSILON);

 

    nfa_free(nfa1);

    nfa_free(nfa2);

 

    return result;

}

 

NFA* nfa_star(NFA* nfa) {

    if (!nfa) return NULL;

 

    NFA* result = nfa_create();

    if (!result) return NULL;

 

    // New start state (also accept for zero occurrences)

    int32_t new_start = nfa_add_state(result, 1);

    result->start_state = new_start;

 

    // Copy original NFA states

    int offset = 1;

    for (int i = 0; i < nfa->num_states; i++) {

        nfa_add_state(result, nfa->states[i].is_accept);

    }

 

    // Copy original transitions

    for (int i = 0; i < nfa->num_transitions; i++) {

        nfa_add_transition(result,

            nfa->transitions[i].from_state + offset,

            nfa->transitions[i].to_state + offset,

            nfa->transitions[i].symbol);

    }

 

    // Epsilon from new start to old start

    nfa_add_transition(result, new_start, nfa->start_state + offset, EPSILON);

 

    // Epsilon from accept states back to old start (for repetition)

    for (int i = 0; i < nfa->num_states; i++) {

        if (nfa->states[i].is_accept) {

            nfa_add_transition(result, i + offset, nfa->start_state + offset, EPSILON);

        }

    }

 

    nfa_free(nfa);

 

    return result;

}

 

NFA* nfa_plus(NFA* nfa) {

    if (!nfa) return NULL;

 

    // a+ is equivalent to a.a*

    NFA* nfa_copy = nfa_create();

 

    // Copy states

    for (int i = 0; i < nfa->num_states; i++) {

        nfa_add_state(nfa_copy, nfa->states[i].is_accept);

    }

 

    // Copy transitions

    for (int i = 0; i < nfa->num_transitions; i++) {

        nfa_add_transition(nfa_copy,

            nfa->transitions[i].from_state,

            nfa->transitions[i].to_state,

            nfa->transitions[i].symbol);

    }

 

    nfa_copy->start_state = nfa->start_state;

 

    // Add loop back from accept states

    for (int i = 0; i < nfa->num_states; i++) {

        if (nfa->states[i].is_accept) {

            nfa_add_transition(nfa_copy, i, nfa->start_state, EPSILON);

        }

    }

 

    nfa_free(nfa);

 

    return nfa_copy;

}

 

// ============================================================================

// Regex Parser

// ============================================================================

 

typedef struct {

    const char* input;

    int pos;

    int length;

} Parser;

 

static void parser_init(Parser* p, const char* input) {

    p->input = input;

    p->pos = 0;

    p->length = strlen(input);

}

 

static char parser_peek(Parser* p) {

    if (p->pos >= p->length) return '\0';

    return p->input[p->pos];

}

 

static char parser_consume(Parser* p) {

    if (p->pos >= p->length) return '\0';

    return p->input[p->pos++];

}

 

static int parser_match(Parser* p, char c) {

    if (parser_peek(p) == c) {

        parser_consume(p);

        return 1;

    }

    return 0;

}

 

// Forward declarations

static NFA* parse_expression(Parser* p);

static NFA* parse_term(Parser* p);

static NFA* parse_factor(Parser* p);

static NFA* parse_atom(Parser* p);

 

static NFA* parse_atom(Parser* p) {

    char c = parser_peek(p);

 

    if (c == '(') {

        parser_consume(p);  // consume '('

        NFA* nfa = parse_expression(p);

        parser_match(p, ')');  // consume ')'

        return nfa;

    }

 

    if (c == '\0' || c == ')' || c == '|' || c == '*' || c == '+' || c == '.' || 

        c == ':' || c == '>' || c == '<') {

        return NULL;

    }

 

    // Literal character

    parser_consume(p);

    return nfa_char(c);

}

 

static NFA* parse_factor(Parser* p) {

    NFA* nfa = parse_atom(p);

    if (!nfa) return NULL;

 

    char c = parser_peek(p);

 

    if (c == '*') {

        parser_consume(p);

        return nfa_star(nfa);

    }

 

    if (c == '+') {

        parser_consume(p);

        return nfa_plus(nfa);

    }

 

    return nfa;

}

 

static NFA* parse_term(Parser* p) {

    NFA* nfa = parse_factor(p);

    if (!nfa) return NULL;

 

    while (1) {

        char c = parser_peek(p);

 

        // Check for concatenation operator or implicit concatenation

        if (c == '.') {

            parser_consume(p);

        }

 

        // Stop at end, closing paren, or OR

        if (c == '\0' || c == ')' || c == '|' || c == ':' || c == '>' || c == '<') {

            break;

        }

 

        NFA* next = parse_factor(p);

        if (!next) break;

 

        nfa = nfa_concat(nfa, next);

    }

 

    return nfa;

}

 

static NFA* parse_expression(Parser* p) {

    NFA* nfa = parse_term(p);

    if (!nfa) return NULL;

 

    while (parser_match(p, '|')) {

        NFA* right = parse_term(p);

        if (!right) break;

        nfa = nfa_or(nfa, right);

    }

 

    return nfa;

}

 

static void parse_length_constraints(Parser* p, NFA* nfa) {

    char c = parser_peek(p);

 

    if (c == ':') {

        // Exact length

        parser_consume(p);

        int length = 0;

        while (isdigit(parser_peek(p))) {

            length = length * 10 + (parser_consume(p) - '0');

        }

        nfa->has_exact_length = 1;

        nfa->exact_length = length;

    }

    else if (c == '>') {

        // Minimum length or range

        parser_consume(p);

        int min_len = 0;

        while (isdigit(parser_peek(p))) {

            min_len = min_len * 10 + (parser_consume(p) - '0');

        }

        nfa->has_min_length = 1;

        nfa->min_length = min_len;

 

        if (parser_peek(p) == '<') {

            // Range: >n<m

            parser_consume(p);

            int max_len = 0;

            while (isdigit(parser_peek(p))) {

                max_len = max_len * 10 + (parser_consume(p) - '0');

            }

            nfa->has_max_length = 1;

            nfa->max_length = max_len;

        }

    }

    else if (c == '<') {

        // Maximum length

        parser_consume(p);

        int length = 0;

        while (isdigit(parser_peek(p))) {

            length = length * 10 + (parser_consume(p) - '0');

        }

        nfa->has_max_length = 1;

        nfa->max_length = length;

    }

}

 

NFA* nfa_from_regex(const char* pattern) {

    Parser p;

    parser_init(&p, pattern);

 

    NFA* nfa = parse_expression(&p);

    if (!nfa) return NULL;

 

    // Parse length constraints

    parse_length_constraints(&p, nfa);

 

    return nfa;

}

 

// ============================================================================

// NFA Matching Engine

// ============================================================================

 

static void epsilon_closure(NFA* nfa, int32_t* states, int32_t* num_states) {

    int changed = 1;

 

    while (changed) {

        changed = 0;

        int current_count = *num_states;

 

        for (int i = 0; i < current_count; i++) {

            int state = states[i];

 

            // Find epsilon transitions from this state

            for (int j = 0; j < nfa->num_transitions; j++) {

                if (nfa->transitions[j].from_state == state &&

                    nfa->transitions[j].symbol == EPSILON) {

 

                    int to_state = nfa->transitions[j].to_state;

 

                    // Check if already in states

                    int found = 0;

                    for (int k = 0; k < *num_states; k++) {

                        if (states[k] == to_state) {

                            found = 1;

                            break;

                        }

                    }

 

                    if (!found && *num_states < MAX_STATES) {

                        states[(*num_states)++] = to_state;

                        changed = 1;

                    }

                }

            }

        }

    }

}

 

int32_t nfa_match(NFA* nfa, const char* str) {

    if (!nfa || !str) return 0;

 

    int str_len = strlen(str);

 

    // Check length constraints

    if (nfa->has_exact_length && str_len != nfa->exact_length) {

        return 0;

    }

    if (nfa->has_min_length && str_len <= nfa->min_length) {

        return 0;

    }

    if (nfa->has_max_length && str_len >= nfa->max_length) {

        return 0;

    }

 

    // Initialize current states with start state

    int32_t current_states[MAX_STATES];

    int32_t num_current = 0;

    current_states[num_current++] = nfa->start_state;

 

    // Epsilon closure of start state

    epsilon_closure(nfa, current_states, &num_current);

 

    // Process each character

    for (int i = 0; i < str_len; i++) {

        char c = str[i];

        int32_t next_states[MAX_STATES];

        int32_t num_next = 0;

 

        // Find transitions on character c

        for (int j = 0; j < num_current; j++) {

            int state = current_states[j];

 

            for (int k = 0; k < nfa->num_transitions; k++) {

                if (nfa->transitions[k].from_state == state &&

                    nfa->transitions[k].symbol == (int32_t)c) {

 

                    int to_state = nfa->transitions[k].to_state;

 

                    // Add to next states if not already there

                    int found = 0;

                    for (int l = 0; l < num_next; l++) {

                        if (next_states[l] == to_state) {

                            found = 1;

                            break;

                        }

                    }

 

                    if (!found && num_next < MAX_STATES) {

                        next_states[num_next++] = to_state;

                    }

                }

            }

        }

 

        // Epsilon closure of next states

        epsilon_closure(nfa, next_states, &num_next);

 

        // Move to next states

        num_current = num_next;

        for (int j = 0; j < num_next; j++) {

            current_states[j] = next_states[j];

        }

 

        // If no states, no match

        if (num_current == 0) return 0;

    }

 

    // Check if any current state is an accept state

    for (int i = 0; i < num_current; i++) {

        if (nfa->states[current_states[i]].is_accept) {

            return 1;

        }

    }

 

    return 0;

}

 

// ============================================================================

// Public API

// ============================================================================

 

RegexPattern* regex_compile(const char* pattern) {

    if (!pattern) return NULL;

 

    RegexPattern* regex = (RegexPattern*)malloc(sizeof(RegexPattern));

    if (!regex) return NULL;

 

    regex->nfa = nfa_from_regex(pattern);

    if (!regex->nfa) {

        free(regex);

        return NULL;

    }

 

    regex->pattern_string = strdup(pattern);

 

    return regex;

}

 

int32_t regex_match(RegexPattern* regex, const char* str) {

    if (!regex || !regex->nfa || !str) return 0;

    return nfa_match(regex->nfa, str);

}

 

void regex_free(RegexPattern* regex) {

    if (!regex) return;

    if (regex->nfa) nfa_free(regex->nfa);

    if (regex->pattern_string) free(regex->pattern_string);

    free(regex);

}

