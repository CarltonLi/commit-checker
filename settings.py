# Commit check settings.

from commitcheck.checkers import Pattern


TAB_PATTERNS = [
    #Pattern(r'\t', 'PTAB', 'Tab'),
]

# (pattern, name, description)
GENERAL_PATTERNS = [
    Pattern(r'[ \t]+[\r]?$', 'PTWS', 'Trailing whitespace'),
    Pattern(r'\b(if|switch|for|while|try)\b[^ \t\.]', 'PS01', 'No space after keywords'),
    Pattern(r'\b(if|else|switch|case|for|while|throw|try|catch|finally)[ \t]{2,}\(',
            'PS02', 'Too many whitespaces after keywords'),
    Pattern(r'}[ \t]{2,}\b(else|catch|finally)\b', 'PS03', 'Too many whitespaces before keywords'),
    Pattern(r'\([ \t]+', 'PS04', 'Space after "("'),
    Pattern(r'[ \t]+\)', 'PS05', 'Space before ")"'),
]

ANDROID_PATTERNS = TAB_PATTERNS + GENERAL_PATTERNS + [
    Pattern(r'\)[ \t]{2,}', 'PS06', 'Too many whitespaces after ")"'),
    Pattern(r'[^ ({}"\'/\\]\{', 'PS07', 'Only allow whitespace and "(/{/}/\"/\'/\\" before "{"'),
    Pattern(r',[^ \t\'"\r]', 'PS08', 'No space after ","'),
    Pattern(r'^[ \t]*\bfor\b.*([^ \t]:|:[^ \t])', 'PS09', 'No space on both sides of ":"'),
    #Pattern(r'[^\r]$', 'PUNX', 'Unix format line end is not allowed'),
]
# Android extra patterns. This can be customized in settigns_local.
ANDROID_EXTRA_PATTERNS = []
ANDROID_IGNORES = [
    r'assets/',
    r'libs/',
    r'res/',
    r'.*/legacy/',
]
ANDROID_CHECKS  = [
    r'.*\.java',
]

IOS_PATTERNS = TAB_PATTERNS + GENERAL_PATTERNS + [
    Pattern(r'[^ ({}"\'@:^/\\]\{', 'PS06', 'Only allow whitespace and "(/{/}/\"/\'/@/:/^/\\" before "{"'),
    Pattern(r'^[ \t]*NSLog', 'PL01', 'NSLog not allowed'),
    Pattern(r'[;{}][ \t]*NSLog', 'PL02', 'NSLog not allowed'),
]
IOS_EXTRA_PATTERNS = []
IOS_IGNORES = [
    r'Pods/',
    r'vendors/',
    r'external/',
    r'frameworks/',
    r'.*/MMCoreDefines\.h'
]
IOS_CHECKS  = [
    r'.*\.[hm]',
    r'.*\.pch',
    r'.*\.strings',
]

# Get local settings. All settings should before this.
try:
    from settings_local import *
except ImportError:
    pass

# Get full settings.
ANDROID_FULL_PATTERNS = ANDROID_PATTERNS + ANDROID_EXTRA_PATTERNS
IOS_FULL_PATTERNS = IOS_PATTERNS + IOS_EXTRA_PATTERNS
