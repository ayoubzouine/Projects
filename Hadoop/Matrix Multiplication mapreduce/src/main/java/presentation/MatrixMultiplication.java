package presentation;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.DoubleWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.input.TextInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;
import org.apache.hadoop.mapreduce.lib.output.TextOutputFormat;
import org.apache.log4j.BasicConfigurator;


public class MatrixMultiplication {

//    public static class MatrixMapper extends Mapper<LongWritable, Text, Text, Text> {
//        IntWritable numRows = new IntWritable(0);
//        IntWritable numCols = new IntWritable(0);
//        IntWritable ctr = new IntWritable(0);
//        @Override
//        public void map(LongWritable key, Text value, Context context) throws IOException, InterruptedException {
//            String[] tokens = value.toString().split(",");
//            if(ctr.get() == 0){
//                numRows.set(Integer.parseInt(tokens[0]));
//                numCols.set(Integer.parseInt(tokens[1]));
//                ctr.set(1);
//            }else{
//                int row = Integer.parseInt(tokens[0]);
//                int col = Integer.parseInt(tokens[1]);
//                double matrixValue = Double.parseDouble(tokens[2]);
//                Text outputKey = new Text();
//                Text outputValue = new Text();
//                if (tokens[3].equals("A")) {
//                    // If the input is from matrix A, emit (j, A_i_j) as key-value pair
//                    for(int i=0;i<numCols.get();i++){
//                        outputKey.set("("+i+","+String.valueOf(col)+")");
//                        outputValue.set(row + "," + matrixValue);
//                        System.out.println("key :"+outputKey+"===>"+outputValue);
//                    }
//
//                } else {
//                    // If the input is from matrix B, emit (i, B_i_j) as key-value pair
//                    for(int i=0;i<numRows.get();i++){
//                        outputKey.set("("+String.valueOf(row)+","+i+")");
//                        outputKey.set("("+String.valueOf(row)+","+i+")");
//                        outputValue.set(col + "," + matrixValue);
//                        System.out.println("key :"+outputKey+"===>"+outputValue);
//                    }
//                }
//                context.write(outputKey, outputValue);
//            }
//
//        }
//    }



    public static void main(String[] args) throws Exception {
        BasicConfigurator.configure();
        Configuration conf = new Configuration() ;
        Job job = Job.getInstance(conf, "max hauteur");
        job.setJarByClass(MatrixMultiplication.class);
        job.setMapperClass(MatrixMapper.class);
        job.setCombinerClass(MatrixReducer.class);
        job.setReducerClass(MatrixReducer.class);
        job.setOutputKeyClass(Text.class);
        job.setOutputValueClass(Text.class);
        FileInputFormat.addInputPath(job, new Path(args[0]));
        FileOutputFormat.setOutputPath(job, new Path(args[1]));
        System.exit(job.waitForCompletion(true) ? 0 : 1);


    }


}