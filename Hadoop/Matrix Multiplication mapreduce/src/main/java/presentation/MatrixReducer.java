package presentation;

import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Reducer;

import java.io.IOException;
import java.util.HashMap;
import java.util.Map;

public  class MatrixReducer extends Reducer<Text, Text, Text, Text> {

    @Override
    public void reduce(Text key, Iterable<Text> values, Context context) throws IOException, InterruptedException {
        Map<Integer, Double> matrixAValues = new HashMap<>();
        Map<Integer, Double> matrixBValues = new HashMap<>();
        for (Text value : values) {
            String[] tokens = value.toString().split(",");
            int index = Integer.parseInt(tokens[0]);
            double matrixValue = Double.parseDouble(tokens[1]);
            if(!matrixAValues.containsKey(index))
                matrixAValues.put(index,matrixValue);
            else matrixBValues.put(index,matrixValue);
        }
        double product = 0.0;
        for (int i = 0; i < matrixAValues.size(); i++) {
            double valueA =  matrixAValues.get(i);
            double valueB = matrixBValues.get(i);
            product += valueA * valueB;
        }
        Text outputKey = new Text();
       Text outputValue = new Text();
       outputKey.set(key.toString());
       outputValue.set(String.valueOf(product));
       context.write(outputKey, outputValue);
    }
}