// Code generated by protoc-gen-go. DO NOT EDIT.
// source: alert/alert.proto

package alert

import (
	context "context"
	fmt "fmt"
	proto "github.com/golang/protobuf/proto"
	grpc "google.golang.org/grpc"
	codes "google.golang.org/grpc/codes"
	status "google.golang.org/grpc/status"
	math "math"
)

// Reference imports to suppress errors if they are not otherwise used.
var _ = proto.Marshal
var _ = fmt.Errorf
var _ = math.Inf

// This is a compile-time assertion to ensure that this generated file
// is compatible with the proto package it is being compiled against.
// A compilation error at this line likely means your copy of the
// proto package needs to be updated.
const _ = proto.ProtoPackageIsVersion3 // please upgrade the proto package

// Event is inspired by Google Analytics events
// https://developers.google.com/analytics/devguides/collection/analyticsjs/events
type Event struct {
	// id is not required for inserts
	Id                   string            `protobuf:"bytes,1,opt,name=id,proto3" json:"id,omitempty"`
	Category             string            `protobuf:"bytes,2,opt,name=category,proto3" json:"category,omitempty"`
	Action               string            `protobuf:"bytes,3,opt,name=action,proto3" json:"action,omitempty"`
	Label                string            `protobuf:"bytes,4,opt,name=label,proto3" json:"label,omitempty"`
	Value                uint64            `protobuf:"varint,5,opt,name=value,proto3" json:"value,omitempty"`
	Metadata             map[string]string `protobuf:"bytes,6,rep,name=metadata,proto3" json:"metadata,omitempty" protobuf_key:"bytes,1,opt,name=key,proto3" protobuf_val:"bytes,2,opt,name=value,proto3"`
	XXX_NoUnkeyedLiteral struct{}          `json:"-"`
	XXX_unrecognized     []byte            `json:"-"`
	XXX_sizecache        int32             `json:"-"`
}

func (m *Event) Reset()         { *m = Event{} }
func (m *Event) String() string { return proto.CompactTextString(m) }
func (*Event) ProtoMessage()    {}
func (*Event) Descriptor() ([]byte, []int) {
	return fileDescriptor_975149e03a08f257, []int{0}
}

func (m *Event) XXX_Unmarshal(b []byte) error {
	return xxx_messageInfo_Event.Unmarshal(m, b)
}
func (m *Event) XXX_Marshal(b []byte, deterministic bool) ([]byte, error) {
	return xxx_messageInfo_Event.Marshal(b, m, deterministic)
}
func (m *Event) XXX_Merge(src proto.Message) {
	xxx_messageInfo_Event.Merge(m, src)
}
func (m *Event) XXX_Size() int {
	return xxx_messageInfo_Event.Size(m)
}
func (m *Event) XXX_DiscardUnknown() {
	xxx_messageInfo_Event.DiscardUnknown(m)
}

var xxx_messageInfo_Event proto.InternalMessageInfo

func (m *Event) GetId() string {
	if m != nil {
		return m.Id
	}
	return ""
}

func (m *Event) GetCategory() string {
	if m != nil {
		return m.Category
	}
	return ""
}

func (m *Event) GetAction() string {
	if m != nil {
		return m.Action
	}
	return ""
}

func (m *Event) GetLabel() string {
	if m != nil {
		return m.Label
	}
	return ""
}

func (m *Event) GetValue() uint64 {
	if m != nil {
		return m.Value
	}
	return 0
}

func (m *Event) GetMetadata() map[string]string {
	if m != nil {
		return m.Metadata
	}
	return nil
}

type ReportEventRequest struct {
	Event                *Event   `protobuf:"bytes,1,opt,name=event,proto3" json:"event,omitempty"`
	XXX_NoUnkeyedLiteral struct{} `json:"-"`
	XXX_unrecognized     []byte   `json:"-"`
	XXX_sizecache        int32    `json:"-"`
}

func (m *ReportEventRequest) Reset()         { *m = ReportEventRequest{} }
func (m *ReportEventRequest) String() string { return proto.CompactTextString(m) }
func (*ReportEventRequest) ProtoMessage()    {}
func (*ReportEventRequest) Descriptor() ([]byte, []int) {
	return fileDescriptor_975149e03a08f257, []int{1}
}

func (m *ReportEventRequest) XXX_Unmarshal(b []byte) error {
	return xxx_messageInfo_ReportEventRequest.Unmarshal(m, b)
}
func (m *ReportEventRequest) XXX_Marshal(b []byte, deterministic bool) ([]byte, error) {
	return xxx_messageInfo_ReportEventRequest.Marshal(b, m, deterministic)
}
func (m *ReportEventRequest) XXX_Merge(src proto.Message) {
	xxx_messageInfo_ReportEventRequest.Merge(m, src)
}
func (m *ReportEventRequest) XXX_Size() int {
	return xxx_messageInfo_ReportEventRequest.Size(m)
}
func (m *ReportEventRequest) XXX_DiscardUnknown() {
	xxx_messageInfo_ReportEventRequest.DiscardUnknown(m)
}

var xxx_messageInfo_ReportEventRequest proto.InternalMessageInfo

func (m *ReportEventRequest) GetEvent() *Event {
	if m != nil {
		return m.Event
	}
	return nil
}

type ReportEventResponse struct {
	XXX_NoUnkeyedLiteral struct{} `json:"-"`
	XXX_unrecognized     []byte   `json:"-"`
	XXX_sizecache        int32    `json:"-"`
}

func (m *ReportEventResponse) Reset()         { *m = ReportEventResponse{} }
func (m *ReportEventResponse) String() string { return proto.CompactTextString(m) }
func (*ReportEventResponse) ProtoMessage()    {}
func (*ReportEventResponse) Descriptor() ([]byte, []int) {
	return fileDescriptor_975149e03a08f257, []int{2}
}

func (m *ReportEventResponse) XXX_Unmarshal(b []byte) error {
	return xxx_messageInfo_ReportEventResponse.Unmarshal(m, b)
}
func (m *ReportEventResponse) XXX_Marshal(b []byte, deterministic bool) ([]byte, error) {
	return xxx_messageInfo_ReportEventResponse.Marshal(b, m, deterministic)
}
func (m *ReportEventResponse) XXX_Merge(src proto.Message) {
	xxx_messageInfo_ReportEventResponse.Merge(m, src)
}
func (m *ReportEventResponse) XXX_Size() int {
	return xxx_messageInfo_ReportEventResponse.Size(m)
}
func (m *ReportEventResponse) XXX_DiscardUnknown() {
	xxx_messageInfo_ReportEventResponse.DiscardUnknown(m)
}

var xxx_messageInfo_ReportEventResponse proto.InternalMessageInfo

func init() {
	proto.RegisterType((*Event)(nil), "alert.Event")
	proto.RegisterMapType((map[string]string)(nil), "alert.Event.MetadataEntry")
	proto.RegisterType((*ReportEventRequest)(nil), "alert.ReportEventRequest")
	proto.RegisterType((*ReportEventResponse)(nil), "alert.ReportEventResponse")
}

func init() { proto.RegisterFile("alert/alert.proto", fileDescriptor_975149e03a08f257) }

var fileDescriptor_975149e03a08f257 = []byte{
	// 268 bytes of a gzipped FileDescriptorProto
	0x1f, 0x8b, 0x08, 0x00, 0x00, 0x00, 0x00, 0x00, 0x02, 0xff, 0x6c, 0x91, 0xcf, 0x4a, 0xc3, 0x40,
	0x10, 0x87, 0x4d, 0xd2, 0x0d, 0x75, 0xa2, 0xa2, 0xe3, 0x1f, 0xd6, 0x9c, 0x42, 0x4e, 0x39, 0x45,
	0x88, 0x20, 0x45, 0x4f, 0x1e, 0xea, 0x4d, 0x84, 0x7d, 0x83, 0x6d, 0x33, 0x48, 0x30, 0x66, 0x63,
	0x32, 0x2d, 0xe4, 0x9d, 0x7d, 0x08, 0xc9, 0x6e, 0xa8, 0x2d, 0x7a, 0x59, 0xf6, 0x9b, 0x6f, 0x76,
	0xe6, 0x07, 0x0b, 0x17, 0xba, 0xa6, 0x8e, 0xef, 0xec, 0x99, 0xb7, 0x9d, 0x61, 0x83, 0xc2, 0x42,
	0xfa, 0xed, 0x81, 0x58, 0x6e, 0xa9, 0x61, 0x3c, 0x03, 0xbf, 0x2a, 0xa5, 0x97, 0x78, 0xd9, 0xb1,
	0xf2, 0xab, 0x12, 0x63, 0x98, 0xaf, 0x35, 0xd3, 0xbb, 0xe9, 0x06, 0xe9, 0xdb, 0xea, 0x8e, 0xf1,
	0x06, 0x42, 0xbd, 0xe6, 0xca, 0x34, 0x32, 0xb0, 0x66, 0x22, 0xbc, 0x02, 0x51, 0xeb, 0x15, 0xd5,
	0x72, 0x66, 0xcb, 0x0e, 0xc6, 0xea, 0x56, 0xd7, 0x1b, 0x92, 0x22, 0xf1, 0xb2, 0x99, 0x72, 0x80,
	0x0f, 0x30, 0xff, 0x24, 0xd6, 0xa5, 0x66, 0x2d, 0xc3, 0x24, 0xc8, 0xa2, 0x22, 0xce, 0x5d, 0x40,
	0x9b, 0x27, 0x7f, 0x9d, 0xe4, 0xb2, 0xe1, 0x6e, 0x50, 0xbb, 0xde, 0xf8, 0x09, 0x4e, 0x0f, 0x14,
	0x9e, 0x43, 0xf0, 0x41, 0xc3, 0x94, 0x7c, 0xbc, 0xfe, 0x2e, 0x74, 0xb9, 0x1d, 0x3c, 0xfa, 0x0b,
	0x2f, 0x5d, 0x00, 0x2a, 0x6a, 0x4d, 0xc7, 0x76, 0x87, 0xa2, 0xaf, 0x0d, 0xf5, 0x8c, 0x29, 0x08,
	0x1a, 0xd9, 0xce, 0x88, 0x8a, 0x93, 0xfd, 0x1c, 0xca, 0xa9, 0xf4, 0x1a, 0x2e, 0x0f, 0x5e, 0xf6,
	0xad, 0x69, 0x7a, 0x2a, 0xde, 0x40, 0x3c, 0x8f, 0xcd, 0xf8, 0x02, 0xd1, 0x9e, 0xc7, 0xdb, 0x69,
	0xc6, 0xdf, 0x6d, 0x71, 0xfc, 0x9f, 0x72, 0xe3, 0xd2, 0xa3, 0x55, 0x68, 0xbf, 0xe7, 0xfe, 0x27,
	0x00, 0x00, 0xff, 0xff, 0x36, 0x3c, 0xb5, 0x2a, 0xb3, 0x01, 0x00, 0x00,
}

// Reference imports to suppress errors if they are not otherwise used.
var _ context.Context
var _ grpc.ClientConn

// This is a compile-time assertion to ensure that this generated file
// is compatible with the grpc package it is being compiled against.
const _ = grpc.SupportPackageIsVersion4

// AlertClient is the client API for Alert service.
//
// For semantics around ctx use and closing/ending streaming RPCs, please refer to https://godoc.org/google.golang.org/grpc#ClientConn.NewStream.
type AlertClient interface {
	// ReportEvent does event ingestions.
	ReportEvent(ctx context.Context, in *ReportEventRequest, opts ...grpc.CallOption) (*ReportEventResponse, error)
}

type alertClient struct {
	cc *grpc.ClientConn
}

func NewAlertClient(cc *grpc.ClientConn) AlertClient {
	return &alertClient{cc}
}

func (c *alertClient) ReportEvent(ctx context.Context, in *ReportEventRequest, opts ...grpc.CallOption) (*ReportEventResponse, error) {
	out := new(ReportEventResponse)
	err := c.cc.Invoke(ctx, "/alert.Alert/ReportEvent", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

// AlertServer is the server API for Alert service.
type AlertServer interface {
	// ReportEvent does event ingestions.
	ReportEvent(context.Context, *ReportEventRequest) (*ReportEventResponse, error)
}

// UnimplementedAlertServer can be embedded to have forward compatible implementations.
type UnimplementedAlertServer struct {
}

func (*UnimplementedAlertServer) ReportEvent(ctx context.Context, req *ReportEventRequest) (*ReportEventResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method ReportEvent not implemented")
}

func RegisterAlertServer(s *grpc.Server, srv AlertServer) {
	s.RegisterService(&_Alert_serviceDesc, srv)
}

func _Alert_ReportEvent_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(ReportEventRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(AlertServer).ReportEvent(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/alert.Alert/ReportEvent",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(AlertServer).ReportEvent(ctx, req.(*ReportEventRequest))
	}
	return interceptor(ctx, in, info, handler)
}

var _Alert_serviceDesc = grpc.ServiceDesc{
	ServiceName: "alert.Alert",
	HandlerType: (*AlertServer)(nil),
	Methods: []grpc.MethodDesc{
		{
			MethodName: "ReportEvent",
			Handler:    _Alert_ReportEvent_Handler,
		},
	},
	Streams:  []grpc.StreamDesc{},
	Metadata: "alert/alert.proto",
}
