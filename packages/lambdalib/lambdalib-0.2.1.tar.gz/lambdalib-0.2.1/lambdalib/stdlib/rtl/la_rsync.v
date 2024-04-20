//#############################################################################
//# Function:  Reset synchronizer (async assert, sync deassert)               #
//# Copyright: Lambda Project Authors. All rights Reserved.                   #
//# License:   MIT (see LICENSE file in Lambda repository)                    #
//#############################################################################

module la_rsync #(
    parameter PROP = "DEFAULT"
) (
    input clk,  // clock
    input nrst_in,  // async reset input
    output nrst_out  // async assert, sync deassert reset
);

    localparam STAGES = 2;
    localparam RND = 1;

    reg     [STAGES:0] sync_pipe;
    integer            sync_delay;

`ifndef SYNTHESIS
    always @(posedge clk) sync_delay <= {$random} % 2;
`endif

    always @(posedge clk or negedge nrst_in)
        if (!nrst_in) sync_pipe[STAGES:0] <= 'b0;
        else sync_pipe[STAGES:0] <= {sync_pipe[STAGES-1:0], 1'b1};

`ifdef SYNTHESIS
    assign nrst_out = sync_pipe[STAGES-1];
`else
    assign nrst_out = (|sync_delay & (|RND)) ? sync_pipe[STAGES] : sync_pipe[STAGES-1];
`endif

endmodule
