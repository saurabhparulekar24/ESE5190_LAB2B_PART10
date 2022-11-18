add_executable(pio_seq)
pico_generate_pio_header(pio_seq ${CMAKE_CURRENT_LIST_DIR}/pio_seq.pio)
target_sources(pio_seq PRIVATE pio_seq.c sio_registers.c pixel.c)



target_link_libraries(pio_seq PRIVATE pico_stdlib hardware_pio hardware_dma)
pico_add_extra_outputs(pio_seq)

pico_enable_stdio_usb(pio_seq 1) # PICO SDK (USB)
pico_enable_stdio_uart(pio_seq 0) # PICO SDK (USB)

# add url via pico_set_program_url
example_auto_set_url(pio_seq)