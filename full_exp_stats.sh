python3.11 trace_extraction.py ../sim_full_lrr/rodinia_1b_5l ./traces_lrr/rodinia_1b_5l
python3.11 trace_extraction.py ../sim_full_lrr/rodinia_1b_10l ./traces_lrr/rodinia_1b_10l
python3.11 trace_extraction.py ../sim_full_lrr/rodinia_1b_25l ./traces_lrr/rodinia_1b_25l
python3.11 trace_extraction.py ../sim_full_lrr/rodinia_1b_50l ./traces_lrr/rodinia_1b_50l
python3.11 trace_extraction.py ../sim_full_lrr/rodinia_1b_100l ./traces_lrr/rodinia_1b_100l
python3.11 trace_extraction.py ../sim_full_lrr/rodinia_1b_200l ./traces_lrr/rodinia_1b_200l
python3.11 trace_extraction.py ../sim_full_lrr/rodinia_1b_400l ./traces_lrr/rodinia_1b_400l
python3.11 trace_extraction.py ../sim_full_gto/rodinia_1b_5l ./traces_gto/rodinia_1b_5l
python3.11 trace_extraction.py ../sim_full_gto/rodinia_1b_10l ./traces_gto/rodinia_1b_10l
python3.11 trace_extraction.py ../sim_full_gto/rodinia_1b_25l ./traces_gto/rodinia_1b_25l
python3.11 trace_extraction.py ../sim_full_gto/rodinia_1b_50l ./traces_gto/rodinia_1b_50l
python3.11 trace_extraction.py ../sim_full_gto/rodinia_1b_100l ./traces_gto/rodinia_1b_100l
python3.11 trace_extraction.py ../sim_full_gto/rodinia_1b_200l ./traces_gto/rodinia_1b_200l
python3.11 trace_extraction.py ../sim_full_gto/rodinia_1b_400l ./traces_gto/rodinia_1b_400l
python3.11 trace_extraction.py ../sim_full_1w/rodinia_1w_5l ./traces_1w/rodinia_1w_5l
python3.11 trace_extraction.py ../sim_full_1w/rodinia_1w_10l ./traces_1w/rodinia_1w_10l
python3.11 trace_extraction.py ../sim_full_1w/rodinia_1w_25l ./traces_1w/rodinia_1w_25l
python3.11 trace_extraction.py ../sim_full_1w/rodinia_1w_50l ./traces_1w/rodinia_1w_50l
python3.11 trace_extraction.py ../sim_full_1w/rodinia_1w_100l ./traces_1w/rodinia_1w_100l
python3.11 trace_extraction.py ../sim_full_1w/rodinia_1w_200l ./traces_1w/rodinia_1w_200l
python3.11 trace_extraction.py ../sim_full_1w/rodinia_1w_400l ./traces_1w/rodinia_1w_400l
python3.11 worst_traces_extraction.py ./traces_lrr/rodinia_1b_5l ./ptx_files ./rodinia_bounds ./exp_rodinia_lrr
python3.11 worst_traces_extraction.py ./traces_lrr/rodinia_1b_10l ./ptx_files ./rodinia_bounds ./exp_rodinia_lrr
python3.11 worst_traces_extraction.py ./traces_lrr/rodinia_1b_25l ./ptx_files ./rodinia_bounds ./exp_rodinia_lrr
python3.11 worst_traces_extraction.py ./traces_lrr/rodinia_1b_50l ./ptx_files ./rodinia_bounds ./exp_rodinia_lrr
python3.11 worst_traces_extraction.py ./traces_lrr/rodinia_1b_100l ./ptx_files ./rodinia_bounds ./exp_rodinia_lrr
python3.11 worst_traces_extraction.py ./traces_lrr/rodinia_1b_200l ./ptx_files ./rodinia_bounds ./exp_rodinia_lrr
python3.11 worst_traces_extraction.py ./traces_lrr/rodinia_1b_400l ./ptx_files ./rodinia_bounds ./exp_rodinia_lrr
python3.11 worst_traces_extraction.py ./traces_gto/rodinia_1b_5l ./ptx_files ./rodinia_bounds ./exp_rodinia_gto
python3.11 worst_traces_extraction.py ./traces_gto/rodinia_1b_10l ./ptx_files ./rodinia_bounds ./exp_rodinia_gto
python3.11 worst_traces_extraction.py ./traces_gto/rodinia_1b_25l ./ptx_files ./rodinia_bounds ./exp_rodinia_gto
python3.11 worst_traces_extraction.py ./traces_gto/rodinia_1b_50l ./ptx_files ./rodinia_bounds ./exp_rodinia_gto
python3.11 worst_traces_extraction.py ./traces_gto/rodinia_1b_100l ./ptx_files ./rodinia_bounds ./exp_rodinia_gto
python3.11 worst_traces_extraction.py ./traces_gto/rodinia_1b_200l ./ptx_files ./rodinia_bounds ./exp_rodinia_gto
python3.11 worst_traces_extraction.py ./traces_gto/rodinia_1b_400l ./ptx_files ./rodinia_bounds ./exp_rodinia_gto
python3.11 worst_traces_extraction.py ./traces_1w/rodinia_1w_5l ./ptx_files ./rodinia_bounds ./exp_rodinia_1w
python3.11 worst_traces_extraction.py ./traces_1w/rodinia_1w_10l ./ptx_files ./rodinia_bounds ./exp_rodinia_1w
python3.11 worst_traces_extraction.py ./traces_1w/rodinia_1w_25l ./ptx_files ./rodinia_bounds ./exp_rodinia_1w
python3.11 worst_traces_extraction.py ./traces_1w/rodinia_1w_50l ./ptx_files ./rodinia_bounds ./exp_rodinia_1w
python3.11 worst_traces_extraction.py ./traces_1w/rodinia_1w_100l ./ptx_files ./rodinia_bounds ./exp_rodinia_1w
python3.11 worst_traces_extraction.py ./traces_1w/rodinia_1w_200l ./ptx_files ./rodinia_bounds ./exp_rodinia_1w
python3.11 worst_traces_extraction.py ./traces_1w/rodinia_1w_400l ./ptx_files ./rodinia_bounds ./exp_rodinia_1w

python3 ../sass-decompiler/src/ptx_graph_experiments.py ./configs/SM86_ORIN_5l_lrr/gpgpusim.config ./exp_rodinia_lrr/rodinia_1b_5l/ 2 ./exp_res.csv
python3 ../sass-decompiler/src/ptx_graph_experiments.py ./configs/SM86_ORIN_5l_gto/gpgpusim.config ./exp_rodinia_gto/rodinia_1b_5l/ 2 ./exp_res.csv
python3 ../sass-decompiler/src/ptx_graph_experiments.py ./configs/SM86_ORIN_5l_lrr/gpgpusim.config ./exp_rodinia_1w/rodinia_1w_5l/ 1 ./exp_res.csv

python3 ../sass-decompiler/src/ptx_graph_experiments.py ./configs/SM86_ORIN_10l_lrr/gpgpusim.config ./exp_rodinia_lrr/rodinia_1b_10l/ 2 ./exp_res.csv
python3 ../sass-decompiler/src/ptx_graph_experiments.py ./configs/SM86_ORIN_10l_gto/gpgpusim.config ./exp_rodinia_gto/rodinia_1b_10l/ 2 ./exp_res.csv
python3 ../sass-decompiler/src/ptx_graph_experiments.py ./configs/SM86_ORIN_10l_lrr/gpgpusim.config ./exp_rodinia_1w/rodinia_1w_10l/ 1 ./exp_res.csv

python3 ../sass-decompiler/src/ptx_graph_experiments.py ./configs/SM86_ORIN_25l_lrr/gpgpusim.config ./exp_rodinia_lrr/rodinia_1b_25l/ 2 ./exp_res.csv
python3 ../sass-decompiler/src/ptx_graph_experiments.py ./configs/SM86_ORIN_25l_gto/gpgpusim.config ./exp_rodinia_gto/rodinia_1b_25l/ 2 ./exp_res.csv
python3 ../sass-decompiler/src/ptx_graph_experiments.py ./configs/SM86_ORIN_25l_lrr/gpgpusim.config ./exp_rodinia_1w/rodinia_1w_25l/ 1 ./exp_res.csv

python3 ../sass-decompiler/src/ptx_graph_experiments.py ./configs/SM86_ORIN_50l_lrr/gpgpusim.config ./exp_rodinia_lrr/rodinia_1b_50l/ 2 ./exp_res.csv
python3 ../sass-decompiler/src/ptx_graph_experiments.py ./configs/SM86_ORIN_50l_gto/gpgpusim.config ./exp_rodinia_gto/rodinia_1b_50l/ 2 ./exp_res.csv
python3 ../sass-decompiler/src/ptx_graph_experiments.py ./configs/SM86_ORIN_50l_lrr/gpgpusim.config ./exp_rodinia_1w/rodinia_1w_50l/ 1 ./exp_res.csv

python3 ../sass-decompiler/src/ptx_graph_experiments.py ./configs/SM86_ORIN_100l_lrr/gpgpusim.config ./exp_rodinia_lrr/rodinia_1b_100l/ 2 ./exp_res.csv
python3 ../sass-decompiler/src/ptx_graph_experiments.py ./configs/SM86_ORIN_100l_gto/gpgpusim.config ./exp_rodinia_gto/rodinia_1b_100l/ 2 ./exp_res.csv
python3 ../sass-decompiler/src/ptx_graph_experiments.py ./configs/SM86_ORIN_100l_lrr/gpgpusim.config ./exp_rodinia_1w/rodinia_1w_100l/ 1 ./exp_res.csv

python3 ../sass-decompiler/src/ptx_graph_experiments.py ./configs/SM86_ORIN_200l_lrr/gpgpusim.config ./exp_rodinia_lrr/rodinia_1b_200l/ 2 ./exp_res.csv
python3 ../sass-decompiler/src/ptx_graph_experiments.py ./configs/SM86_ORIN_200l_gto/gpgpusim.config ./exp_rodinia_gto/rodinia_1b_200l/ 2 ./exp_res.csv
python3 ../sass-decompiler/src/ptx_graph_experiments.py ./configs/SM86_ORIN_200l_lrr/gpgpusim.config ./exp_rodinia_1w/rodinia_1w_200l/ 1 ./exp_res.csv

python3 ../sass-decompiler/src/ptx_graph_experiments.py ./configs/SM86_ORIN_400l_lrr/gpgpusim.config ./exp_rodinia_lrr/rodinia_1b_400l/ 2 ./exp_res.csv
python3 ../sass-decompiler/src/ptx_graph_experiments.py ./configs/SM86_ORIN_400l_gto/gpgpusim.config ./exp_rodinia_gto/rodinia_1b_400l/ 2 ./exp_res.csv
python3 ../sass-decompiler/src/ptx_graph_experiments.py ./configs/SM86_ORIN_400l_lrr/gpgpusim.config ./exp_rodinia_1w/rodinia_1w_400l/ 1 ./exp_res.csv