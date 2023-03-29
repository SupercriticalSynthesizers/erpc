flex_options = []

if host_machine.system() == 'windows'
    winflexbison_proj = subproject('winflexbison')
    
    flex_options += '--wincompat'
endif

pymod = import('python')

bison = find_program([
    '/opt/homebrew/opt/bison/bin/bison',
    'bison'
])
flex = find_program('flex')
python = pymod.find_installation()

# Build lexer & parser
lexer_target = custom_target(
    input: 'src/erpcgen_lexer.l',
    output: 'erpcgen_lexer.cpp',
    command: [flex, flex_options, '-o', '@OUTPUT@', '@INPUT@']
)

parser_target = custom_target(
    input: 'src/erpcgen_parser.y',
    output: [
        'erpcgen_parser.tab.cpp',
        'erpcgen_parser.tab.hpp'
    ],
    command: [bison, '-o', '@OUTPUT0@', '@INPUT@', '-Wnone']
)

# Convert templates to C sources.
templates = [
    'c_client_source',
    'c_coders',
    'c_common_functions',
    'c_common_header',
    'c_crc',
    'c_server_header',
    'c_server_source',
    'py_client',
    'py_coders',
    'py_common',
    'py_global_init',
    'py_init',
    'py_interface',
    'py_server',
]

template_targets = []

foreach template : templates
    template_targets += custom_target(
        input: 'src/templates' / template + '.template',
        output: template + '.c',
        command: [python, '@CURRENT_SOURCE_DIR@/bin/txt_to_c.py', '-o', '@OUTPUT@', '@INPUT@'],
    )
endforeach

includes = [
    '.',
    '..',
    '../erpc_c/infra',
    'src',
    'src/cpptemplate',
    'src/types',
]

sources = [
    '../erpc_c/infra/erpc_crc16.cpp',
    'src/types/Type.cpp',
    'src/AstNode.cpp',
    'src/AstWalker.cpp',
    'src/CGenerator.cpp',
    'src/cpptemplate/cpptempl.cpp',
    'src/erpcgen.cpp',
    'src/ErpcLexer.cpp',
    'src/format_string.cpp',
    'src/Generator.cpp',
    'src/HexValues.cpp',
    'src/InterfaceDefinition.cpp',
    'src/Logging.cpp',
    'src/options.cpp',
    'src/ParseErrors.cpp',
    'src/PythonGenerator.cpp',
    'src/SearchPath.cpp',
    'src/SymbolScanner.cpp',
    'src/Token.cpp',
    'src/UniqueIdChecker.cpp',
    'src/Utils.cpp',
    lexer_target,
    parser_target,
    template_targets,
]

deps = [
    dependency('boost',
        modules: ['filesystem', 'system'],
        static: true,
        native: true,
    ),
]

common_args = []

if host_machine.system() == 'windows'
    winflexbison_dep = winflexbison_proj.get_variable('winflexbison_dep')

    includes += 'VisualStudio_v14'
    deps += winflexbison_dep
    common_args += '-DWIN32'
endif

erpcgen_exe = executable('erpcgen',
    sources: sources,
    include_directories: includes,
    dependencies: deps,

    c_args: common_args,
    cpp_args: common_args,

    native: true,
)
