$(function() {
		var d1 = [[2, 0.039], [3, 0.047], [4, 0.045], [5, 0.033], [6, 0.05], [7, 0.115], [8, 0.690], [9, 7.361], [10, 198.191]];
		var d2 = [[2, 0.03], [3, 0.033], [4, 0.035], [5, 0.031], [6, 0.045], [7, 0.041], [8, 0.035], [9, 0.035], [10, 0.034]];
		var data1 = [{data: d1, label: "Permutations"},
				{data: d2, label: "Closer neighbour"}];
		$.plot($("#speed"), data1);
 });
