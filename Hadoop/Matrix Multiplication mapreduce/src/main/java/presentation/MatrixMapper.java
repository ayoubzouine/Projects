package presentation;

import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;

import java.io.IOException;

public class MatrixMapper extends Mapper<LongWritable, Text,Text, Text> {
    IntWritable ctr = new IntWritable(0);
    IntWritable numRows = new IntWritable(0);
    IntWritable numCols = new IntWritable(0);
    @Override
    public void map(LongWritable key, Text value, Context context) throws IOException, InterruptedException {
        // token  =  ligne
        String[] tokens = value.toString().split(",");
        if(ctr.get() == 0){
            numRows.set(Integer.parseInt(tokens[0]));
            numCols.set(Integer.parseInt(tokens[1]));
            ctr.set(1);
        }else{
            int row = Integer.parseInt(tokens[1]);
            int col = Integer.parseInt(tokens[2]);
            double matrixValue = Double.parseDouble(tokens[3]);
            Text outputKey = new Text();
            Text outputValue = new Text();
            if (tokens[0].equals("A")) {
                for(int i=0;i<numCols.get();i++){
                    outputKey.set(String.valueOf(row)+","+i);
                    outputValue.set(col + "," + matrixValue);
                    System.out.println("key :"+outputKey+"===>"+outputValue);
                    context.write(outputKey, outputValue);
                }

            } else {

                for(int i=0;i<numRows.get();i++){
                    outputKey.set(i+","+String.valueOf(col));
                    outputValue.set(row + "," + matrixValue);
                    System.out.println("key :"+outputKey+"===>"+outputValue);
                    context.write(outputKey, outputValue);
                }
            }
        }

    }
}
