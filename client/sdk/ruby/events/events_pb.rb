# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: events/events.proto

require 'google/protobuf'

Google::Protobuf::DescriptorPool.generated_pool.build do
  add_message "events.PublishRequest" do
    optional :topic, :string, 1
    map :metadata, :string, :string, 2
    optional :payload, :bytes, 3
    optional :timestamp, :int64, 4
  end
  add_message "events.PublishResponse" do
  end
  add_message "events.SubscribeRequest" do
    optional :queue, :string, 1
    optional :topic, :string, 2
    optional :start_at_time, :int64, 3
    optional :auto_ack, :bool, 4
    optional :ack_wait, :int64, 5
    optional :retry_limit, :int64, 6
  end
  add_message "events.Event" do
    optional :id, :string, 1
    optional :topic, :string, 2
    map :metadata, :string, :string, 3
    optional :payload, :bytes, 4
    optional :timestamp, :int64, 5
  end
  add_message "events.ReadRequest" do
    optional :topic, :string, 1
    optional :limit, :uint64, 2
    optional :offset, :uint64, 3
  end
  add_message "events.ReadResponse" do
    repeated :events, :message, 1, "events.Event"
  end
  add_message "events.WriteRequest" do
    optional :event, :message, 1, "events.Event"
    optional :ttl, :int64, 2
  end
  add_message "events.WriteResponse" do
  end
  add_message "events.AckRequest" do
    optional :id, :string, 1
    optional :success, :bool, 2
  end
end

module Events
  PublishRequest = Google::Protobuf::DescriptorPool.generated_pool.lookup("events.PublishRequest").msgclass
  PublishResponse = Google::Protobuf::DescriptorPool.generated_pool.lookup("events.PublishResponse").msgclass
  SubscribeRequest = Google::Protobuf::DescriptorPool.generated_pool.lookup("events.SubscribeRequest").msgclass
  Event = Google::Protobuf::DescriptorPool.generated_pool.lookup("events.Event").msgclass
  ReadRequest = Google::Protobuf::DescriptorPool.generated_pool.lookup("events.ReadRequest").msgclass
  ReadResponse = Google::Protobuf::DescriptorPool.generated_pool.lookup("events.ReadResponse").msgclass
  WriteRequest = Google::Protobuf::DescriptorPool.generated_pool.lookup("events.WriteRequest").msgclass
  WriteResponse = Google::Protobuf::DescriptorPool.generated_pool.lookup("events.WriteResponse").msgclass
  AckRequest = Google::Protobuf::DescriptorPool.generated_pool.lookup("events.AckRequest").msgclass
end