python3.11 trace_extraction.py ../kalman_lrr/kalman_5l ./kalman_traces_lrr/kalman_5l
python3.11 trace_extraction.py ../kalman_lrr/kalman_10l ./kalman_traces_lrr/kalman_10l
python3.11 trace_extraction.py ../kalman_lrr/kalman_25l ./kalman_traces_lrr/kalman_25l
python3.11 trace_extraction.py ../kalman_lrr/kalman_50l ./kalman_traces_lrr/kalman_50l
python3.11 trace_extraction.py ../kalman_lrr/kalman_100l ./kalman_traces_lrr/kalman_100l
python3.11 trace_extraction.py ../kalman_lrr/kalman_200l ./kalman_traces_lrr/kalman_200l
python3.11 trace_extraction.py ../kalman_lrr/kalman_400l ./kalman_traces_lrr/kalman_400l

python3.11 trace_extraction.py ../kalman_gto/kalman_5l ./kalman_traces_gto/kalman_5l
python3.11 trace_extraction.py ../kalman_gto/kalman_10l ./kalman_traces_gto/kalman_10l
python3.11 trace_extraction.py ../kalman_gto/kalman_25l ./kalman_traces_gto/kalman_25l
python3.11 trace_extraction.py ../kalman_gto/kalman_50l ./kalman_traces_gto/kalman_50l
python3.11 trace_extraction.py ../kalman_gto/kalman_100l ./kalman_traces_gto/kalman_100l
python3.11 trace_extraction.py ../kalman_gto/kalman_200l ./kalman_traces_gto/kalman_200l
python3.11 trace_extraction.py ../kalman_gto/kalman_400l ./kalman_traces_gto/kalman_400l


python3.11 worst_traces_extraction.py ./kalman_traces_lrr/kalman_5l ./ptx_files ./kalman_bounds ./exp_kalman_lrr
python3.11 worst_traces_extraction.py ./kalman_traces_lrr/kalman_10l ./ptx_files ./kalman_bounds ./exp_kalman_lrr
python3.11 worst_traces_extraction.py ./kalman_traces_lrr/kalman_25l ./ptx_files ./kalman_bounds ./exp_kalman_lrr
python3.11 worst_traces_extraction.py ./kalman_traces_lrr/kalman_50l ./ptx_files ./kalman_bounds ./exp_kalman_lrr
python3.11 worst_traces_extraction.py ./kalman_traces_lrr/kalman_100l ./ptx_files ./kalman_bounds ./exp_kalman_lrr
python3.11 worst_traces_extraction.py ./kalman_traces_lrr/kalman_200l ./ptx_files ./kalman_bounds ./exp_kalman_lrr
python3.11 worst_traces_extraction.py ./kalman_traces_lrr/kalman_400l ./ptx_files ./kalman_bounds ./exp_kalman_lrr

python3.11 worst_traces_extraction.py ./kalman_traces_gto/kalman_5l ./ptx_files ./kalman_bounds ./exp_kalman_gto
python3.11 worst_traces_extraction.py ./kalman_traces_gto/kalman_10l ./ptx_files ./kalman_bounds ./exp_kalman_gto
python3.11 worst_traces_extraction.py ./kalman_traces_gto/kalman_25l ./ptx_files ./kalman_bounds ./exp_kalman_gto
python3.11 worst_traces_extraction.py ./kalman_traces_gto/kalman_50l ./ptx_files ./kalman_bounds ./exp_kalman_gto
python3.11 worst_traces_extraction.py ./kalman_traces_gto/kalman_100l ./ptx_files ./kalman_bounds ./exp_kalman_gto
python3.11 worst_traces_extraction.py ./kalman_traces_gto/kalman_200l ./ptx_files ./kalman_bounds ./exp_kalman_gto
python3.11 worst_traces_extraction.py ./kalman_traces_gto/kalman_400l ./ptx_files ./kalman_bounds ./exp_kalman_gto


python3 ../sass-decompiler/src/ptx_graph_experiments.py ./configs/SM86_ORIN_5l_lrr/gpgpusim.config ./exp_kalman_lrr/kalman_5l/ 2 ./kalman_res.csv
python3 ../sass-decompiler/src/ptx_graph_experiments.py ./configs/SM86_ORIN_5l_gto/gpgpusim.config ./exp_kalman_gto/kalman_5l/ 2 ./kalman_res.csv

python3 ../sass-decompiler/src/ptx_graph_experiments.py ./configs/SM86_ORIN_10l_lrr/gpgpusim.config ./exp_kalman_lrr/kalman_10l/ 2 ./kalman_res.csv
python3 ../sass-decompiler/src/ptx_graph_experiments.py ./configs/SM86_ORIN_10l_gto/gpgpusim.config ./exp_kalman_gto/kalman_10l/ 2 ./kalman_res.csv

python3 ../sass-decompiler/src/ptx_graph_experiments.py ./configs/SM86_ORIN_25l_lrr/gpgpusim.config ./exp_kalman_lrr/kalman_25l/ 2 ./kalman_res.csv
python3 ../sass-decompiler/src/ptx_graph_experiments.py ./configs/SM86_ORIN_25l_gto/gpgpusim.config ./exp_kalman_gto/kalman_25l/ 2 ./kalman_res.csv

python3 ../sass-decompiler/src/ptx_graph_experiments.py ./configs/SM86_ORIN_50l_lrr/gpgpusim.config ./exp_kalman_lrr/kalman_50l/ 2 ./kalman_res.csv
python3 ../sass-decompiler/src/ptx_graph_experiments.py ./configs/SM86_ORIN_50l_gto/gpgpusim.config ./exp_kalman_gto/kalman_50l/ 2 ./kalman_res.csv

python3 ../sass-decompiler/src/ptx_graph_experiments.py ./configs/SM86_ORIN_100l_lrr/gpgpusim.config ./exp_kalman_lrr/kalman_100l/ 2 ./kalman_res.csv
python3 ../sass-decompiler/src/ptx_graph_experiments.py ./configs/SM86_ORIN_100l_gto/gpgpusim.config ./exp_kalman_gto/kalman_100l/ 2 ./kalman_res.csv

python3 ../sass-decompiler/src/ptx_graph_experiments.py ./configs/SM86_ORIN_200l_lrr/gpgpusim.config ./exp_kalman_lrr/kalman_200l/ 2 ./kalman_res.csv
python3 ../sass-decompiler/src/ptx_graph_experiments.py ./configs/SM86_ORIN_200l_gto/gpgpusim.config ./exp_kalman_gto/kalman_200l/ 2 ./kalman_res.csv

python3 ../sass-decompiler/src/ptx_graph_experiments.py ./configs/SM86_ORIN_400l_lrr/gpgpusim.config ./exp_kalman_lrr/kalman_400l/ 2 ./kalman_res.csv
python3 ../sass-decompiler/src/ptx_graph_experiments.py ./configs/SM86_ORIN_400l_gto/gpgpusim.config ./exp_kalman_gto/kalman_400l/ 2 ./kalman_res.csv