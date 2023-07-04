import numpy as np
import tensorflow as tf

from dialogue_processor import chat_history_to_dialogue

dishka = 441515260
me = 678562910

# Retrieving training data
texts = chat_history_to_dialogue(user_id=dishka)
input_texts = texts[me]
target_texts = texts[dishka]

# Create token dictionaries
input_tokens = set()
target_tokens = set()

for input_text, target_text in zip(input_texts, target_texts):
    input_tokens.update(input_text)
    target_tokens.update(target_text)

input_token_index = {token: i for i, token in enumerate(input_tokens)}
target_token_index = {token: i for i, token in enumerate(target_tokens)}

# Determine max sequence lengths
max_encoder_seq_length = max(len(input_text) for input_text in input_texts)
max_decoder_seq_length = max(len(target_text) for target_text in target_texts)

# Find the corresponding text for max sequence length
max_encoder_text = next(input_text for input_text in input_texts if len(input_text) == max_encoder_seq_length)
max_decoder_text = next(target_text for target_text in target_texts if len(target_text) == max_decoder_seq_length)

# Print the results
print("Max Encoder Sequence Length:", max_encoder_seq_length)
print("Corresponding Encoder Text:", max_encoder_text)
print("Max Decoder Sequence Length:", max_decoder_seq_length)
print("Corresponding Decoder Text:", max_decoder_text)

# # Generator function for data batches
# def data_generator(batch_size):
#     while True:
#         for start in range(0, len(input_texts), batch_size):
#             end = start + batch_size
#
#             encoder_input_data = np.zeros(
#                 (batch_size, max_encoder_seq_length, len(input_tokens)), dtype="float32"
#             )
#             decoder_input_data = np.zeros(
#                 (batch_size, max_decoder_seq_length, len(target_tokens)), dtype="float32"
#             )
#             decoder_target_data = np.zeros(
#                 (batch_size, max_decoder_seq_length, len(target_tokens)), dtype="float32"
#             )
#
#             batch_input_texts = input_texts[start:end]
#             batch_target_texts = target_texts[start:end]
#
#             for i, (input_text, target_text) in enumerate(zip(batch_input_texts, batch_target_texts)):
#                 for t, char in enumerate(input_text):
#                     encoder_input_data[i, t, input_token_index[char]] = 1.0
#                 for t, char in enumerate(target_text):
#                     decoder_input_data[i, t, target_token_index[char]] = 1.0
#                     if t > 0:
#                         decoder_target_data[i, t - 1, target_token_index[char]] = 1.0
#
#             yield [encoder_input_data, decoder_input_data], decoder_target_data
#
#
# # Define model architecture
# encoder_inputs = tf.keras.Input(shape=(None, len(input_tokens)))
# encoder_lstm = tf.keras.layers.LSTM(units=256, return_state=True)
# encoder_outputs, state_h, state_c = encoder_lstm(encoder_inputs)
# encoder_states = [state_h, state_c]
#
# decoder_inputs = tf.keras.Input(shape=(None, len(target_tokens)))
# decoder_lstm = tf.keras.layers.LSTM(units=256, return_sequences=True, return_state=True)
# decoder_outputs, _, _ = decoder_lstm(decoder_inputs, initial_state=encoder_states)
# decoder_dense = tf.keras.layers.Dense(units=len(target_tokens), activation="softmax")
# decoder_outputs = decoder_dense(decoder_outputs)
#
# model = tf.keras.Model([encoder_inputs, decoder_inputs], decoder_outputs)
#
# # Compile the model
# model.compile(optimizer="adam", loss="categorical_crossentropy")
#
# # Set batch size
# batch_size = 32
#
# # Determine the number of steps per epoch
# steps_per_epoch = len(input_texts) // batch_size
#
# # Train the model using generator function
# model.fit(data_generator(batch_size), steps_per_epoch=steps_per_epoch, epochs=10)
#
# # Save the trained model for future use
# model.save("seq2seq_model.h5")
