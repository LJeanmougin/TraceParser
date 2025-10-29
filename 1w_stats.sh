python3.11 trace_extraction.py ../rodinia_1w_5l_alternative_test ./traces/rodinia_1w_5l_alternative_test
# python3.11 trace_extraction.py ../rodinia_1w_5l_fix_test ./traces/rodinia_1w_5l_fix_test
# python3.11 trace_extraction.py ../ecrts_1w_10l ./traces/ecrts_1w_10l
# python3.11 trace_extraction.py ../ecrts_1w_25l ./traces/ecrts_1w_25l
# python3.11 trace_extraction.py ../ecrts_1w_50l ./traces/ecrts_1w_50l
# python3.11 trace_extraction.py ../ecrts_1w_100l ./traces/ecrts_1w_100l
# python3.11 trace_extraction.py ../ecrts_1w_200l ./traces/ecrts_1w_200l
# python3.11 trace_extraction.py ../ecrts_1w_400l ./traces/ecrts_1w_400l
# python3.11 ../sass-decompiler/src/ptx_experiments.py ./configs/SM86_ORIN_400l_lrr/gpgpusim.config ./traces/ecrts_1w_400l /dev/null
# python3.11 ../sass-decompiler/src/ptx_experiments.py ./configs/SM86_ORIN_200l_lrr/gpgpusim.config ./traces/ecrts_1w_200l /dev/null
# python3.11 ../sass-decompiler/src/ptx_experiments.py ./configs/SM86_ORIN_100l_lrr/gpgpusim.config ./traces/ecrts_1w_100l /dev/null
# python3.11 ../sass-decompiler/src/ptx_experiments.py ./configs/SM86_ORIN_50l_lrr/gpgpusim.config ./traces/ecrts_1w_50l /dev/null
# python3.11 ../sass-decompiler/src/ptx_experiments.py ./configs/SM86_ORIN_25l_lrr/gpgpusim.config ./traces/ecrts_1w_25l /dev/null
# python3.11 ../sass-decompiler/src/ptx_experiments.py ./configs/SM86_ORIN_10l_lrr/gpgpusim.config ./traces/ecrts_1w_10l /dev/null
# python3.11 ../sass-decompiler/src/ptx_experiments.py ./configs/SM86_ORIN_5l_lrr/gpgpusim.config ./traces/rodinia_1w_5l_fix_test /dev/null
python3.11 ../sass-decompiler/src/ptx_trace_experiments.py ./configs/SM86_ORIN_5l_lrr/gpgpusim.config ./traces/rodinia_1w_5l_alternative_test /dev/null
