module main(
      input X,Y;
      output F;
);

assign F = (X&&Y)||(X&&(!Y))||((!X)&&(!Y));
endmodule
