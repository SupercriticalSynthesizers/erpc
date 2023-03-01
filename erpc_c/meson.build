includes = [
    'config',
    'infra',
    'port',
    'setup',
    'transports',
]

sources = [
    'infra/erpc_basic_codec.cpp',
    'infra/erpc_client_manager.cpp',
    'infra/erpc_crc16.cpp',
    'infra/erpc_framed_transport.cpp',
    'infra/erpc_message_buffer.cpp',
    'infra/erpc_message_loggers.cpp',
    'infra/erpc_server.cpp',
    'infra/erpc_simple_server.cpp',
    'infra/erpc_pre_post_action.cpp',
    'setup/erpc_setup_mbf_static.cpp',
    'setup/erpc_server_setup.cpp',
]

erpc_c_lib = library('erpc_c',
    sources: sources,
    include_directories: includes,
)

erpc_c_dep = declare_dependency(
    include_directories: includes,
    link_with: erpc_c_lib,
)
